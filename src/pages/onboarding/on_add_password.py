import flet as ft
import time
from extras.store import RStockStore
from components.rstocknotif import rstocknotif
from extras.tools import validate_password
from argon2 import PasswordHasher
from models.shop import Shop
from models.user import User
from extras.enums import AccountTypeEnums



def on_add_password(page) -> ft.Control:

    store = RStockStore(page=page)

    password_field = ft.TextField(hint_text="*Entrer votre mot de passe", border_radius=10, password=True, can_reveal_password=True)
    password_confirm_field = ft.TextField(hint_text="*Confirmer votre mot de passe", border_radius=10, password=True, can_reveal_password=True)

    def set_shop_user(password):
        shop = store.get("shop_infos")
        shop_name = shop["name"]
        shop_email = shop["email"]
        shop_phone = shop["phone"]
        shop_adress = shop["adress"]
        shop_ifu = shop["ifu"]
        shop_rccm = shop["rccm"]
        shop_logo = shop["logo"]
        shop_first_name = shop["first_name"]
        shop_last_name = shop["last_name"]
        
        shop = Shop(name=shop_name, logo=shop_logo, email=shop_email, phone=shop_phone, adress=shop_adress, balance=0, ifu=shop_ifu, rccm=shop_rccm, manager=f"{shop_first_name} {shop_last_name}")
        shop.save()
        password=PasswordHasher.hash(password)
        admin_user = User(first_name=shop_first_name, last_name=shop_last_name, email=shop_email, phone=shop_phone, password=password, account_type=AccountTypeEnums.OWNER.value)
        admin_user.save()


        
    
    def form_handler(e):

        password = password_field.value.strip()
        password_confirm = password_confirm_field.value.strip()

        password_is_valid, errors = validate_password(password, 4, 128, False, False, False, False, True)

        if password_is_valid:
            password_field.error_text = None
            if password==password_confirm:
                password_field.error_text = None
                password_confirm_field.error_text = None
                set_shop_user(password=password)

            else:
                password_field.error_text = "Erreur ! Le mots de passes ne correspondent pas"
                password_confirm_field.error_text = "Erreur ! Le mots de passes ne correspondent pas"

        else:
            error = ""
            for e in errors:
                error+=f"{e}\n"

            password_field.error_text = error
        
        page.update()

    save_shop_info = ft.ElevatedButton(
        "Enregistrer Mot de Passe",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(10),
            padding=ft.padding.symmetric(vertical=15),
            bgcolor=ft.Colors.SECONDARY,
            text_style=ft.TextStyle(
                font_family="PoppinsMedium",
                size=16
            )
        ),
        icon=ft.Icons.LOCK_OUTLINED,
        color=ft.Colors.ON_SURFACE, 
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
                            ft.Row(controls=[save_shop_info], expand=True)

                    ],
                    spacing=20,
                ),
                padding=ft.padding.only(right=18)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    return add_password_container

