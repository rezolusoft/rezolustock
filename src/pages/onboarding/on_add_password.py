import flet as ft
import time
from core.store import RStockStore
from components.rstocknotif import rstocknotif
from utils.tools import validate_password
from argon2 import PasswordHasher
from datetime import datetime
import asyncio
from models.shop import Shop
from models.user import User
from utils.enums import AccountTypeEnums



def on_add_password(page) -> ft.Control:

    store = RStockStore()

    password_field = ft.TextField(hint_text="*Entrer votre mot de passe", border_radius=10, password=True, can_reveal_password=True, expand=1)
    password_confirm_field = ft.TextField(hint_text="*Confirmer votre mot de passe", border_radius=10, password=True, can_reveal_password=True, expand=1)

    async def set_shop_user(password):
        shop = await store.get_shop()
        shop_name = shop["name"]
        shop_email = shop["email"]
        shop_phone = shop["phone"]
        shop_adress = shop["adress"]
        shop_ifu = shop["ifu"]
        shop_rccm = shop["rccm"]
        shop_logo = shop["logo"]
        shop_first_name = shop["first_name"]
        shop_last_name = shop["last_name"]
        
        new_shop = Shop(
            name=shop_name, 
            logo=shop_logo, 
            email=shop_email, 
            phone=shop_phone, 
            adress=shop_adress, 
            balance=0, 
            ifu=shop_ifu, 
            rccm=shop_rccm, 
            manager=f"{shop_first_name} {shop_last_name}"
            )
        
        new_shop.save()

        hasher = PasswordHasher()
        password=hasher.hash(password)
        admin_user = User(
            first_name=shop_first_name, 
            last_name=shop_last_name, 
            email=shop_email, 
            phone=shop_phone, 
            password=password, 
            account_type=AccountTypeEnums.OWNER.value)
        admin_user.save()
        
        notif = rstocknotif("Opération réussie ✅", "Votre compte administrateur à été crée avec succès !", [])

        await store.set_onboarding_step("on_add_category")

        #login process
        # TODO : Centralize this logic in a complet authentication class including registration + base_user_creation + permissions
        user = User.get(User.email == shop_email)
        user.last_seen=datetime.now()
        user.save()
        user=user.__data__.copy()

        shop_data = Shop.get(Shop.email==shop_email).__data__.copy()

        # quick fix for login
        user.pop("password", None)
        user.pop("created_at", None)
        user.pop("updated_at", None)
        user.pop("deleted", None)

        shop_data.pop("created_at", None)
        shop_data.pop("updated_at", None)
        shop_data.pop("deleted", None)

        user["shop"] = shop_data
        await store.set_user_data(user)
        await store.clear_shop()
        await store.set_onboarding_step("on_add_category")
        
        page.show_dialog(notif)
        await asyncio.sleep(3.5)
        page.pop_dialog()
        await page.push_route("/on_add_category")
        
    
    async def form_handler(e):

        password = password_field.value.strip()
        password_confirm = password_confirm_field.value.strip()

        password_is_valid, errors = validate_password(password, 4, 128, False, False, False, False, True)

        if password_is_valid:
            password_field.error = None
            if password==password_confirm:
                password_field.error = None
                password_confirm_field.error = None
                await set_shop_user(password=password)

            else:
                password_field.error = "Erreur ! Le mots de passes ne correspondent pas"
                password_confirm_field.error = "Erreur ! Le mots de passes ne correspondent pas"

        else:
            error = ""
            for e in errors:
                error+=f"{e}\n"

            password_field.error = error
        
        page.update()

    save_user_info = ft.Button(
        "Enregistrer Mot de Passe",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            padding=ft.Padding.symmetric(vertical=15),
            bgcolor=ft.Colors.SECONDARY,
            text_style=ft.TextStyle(
                font_family="PoppinsMedium",
                size=16
            )
        ),
        icon=ft.Icons.LOCK_OUTLINED,
        color=ft.Colors.WHITE, 
        expand=1,
        on_click=form_handler
        )
    add_password_container = ft.Column(
        controls=[
            ft.Container(
                ft.Column(
            
                    controls=[
                        
                            ft.Row([ft.Text("Définir Un Mot De Passe", size=25, font_family="PoppinsBold",  color=ft.Colors.ON_SURFACE)]),
                            ft.Text("Veuillez définir un mot de passe lié à votre compte administrateur.", size=16, font_family="Poppins", color=ft.Colors.ON_SURFACE),
                            password_field,
                            password_confirm_field,
                            ft.Row(controls=[save_user_info], expand=True)

                    ],
                    spacing=20,
                ),
                padding=ft.Padding.only(right=18)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    return add_password_container

