import flet as ft
import asyncio
from core.store import RStockStore
from core.state import RstockState
from utils.validators import is_valid_email
from core.auth import RstockAuthentication
from components.notification import rstocknotif


async def login(page) -> ft.Control:


    store = RStockStore()
    state = RstockState(page)
    shop = await store.get_shop()

    email_field = ft.TextField(hint_text="Email de connexion", border_radius=5, expand=1, color=ft.Colors.PRIMARY)
    password_field = ft.TextField(hint_text="Votre mot de passe", border_radius=5, password=True, can_reveal_password=True, expand=1, color=ft.Colors.PRIMARY)

    persist_session = ft.Checkbox(label="Se souvenir de moi", value=False, label_style=ft.TextStyle(color=ft.Colors.PRIMARY))

    async def form_handler():
        
        email = email_field.value.strip()
        password = password_field.value.strip()
        persist = persist_session.value
        
        if is_valid_email(email):
            auth = RstockAuthentication(state, store)
            user = await auth.login(email, password, persist)
            if user:
                notif = rstocknotif("Succès ✅", "Accès autorisé. Chargement de votre espace…", [])
                page.show_dialog(notif)
                await asyncio.sleep(1.7)
                page.pop_dialog()
                await page.push_route("/dashboard")
            
            else:
                email_field.error = "Email ou mot de passe incorrect !"
                password_field.error = "Email ou mot de passe incorrect !"
                
                
        else:
            email_field.error = "Veuillez renseigner une adresse email valide"
        
        page.update()
    
    login_button = ft.Button(
        "Connexion",
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
    content = ft.Column(
        controls=[
            ft.Container(
                ft.Column(
            
                    controls=[
                            ft.Image(f"{shop.get('logo')}", width=100),
                            ft.Text(f"Bienvenue | {shop.get("name").capitalize()}", size=25, font_family="PoppinsBold",  color=ft.Colors.ON_SURFACE),
                            ft.Text("Connectez-vous pour continuer à gérer efficacement votre stock et suivre vos performances.", size=16, font_family="Poppins", color=ft.Colors.ON_SURFACE),
                            email_field,
                            password_field,
                            persist_session,
                            ft.Row(controls=[login_button], expand=True)
                    ],
                    spacing=20,
                ),
                padding=ft.Padding.only(right=18)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    login = ft.Container(

        content=ft.Container(

            content=ft.Row(
                controls=[
                    ft.Container(content=content, expand=1),
                    ft.Container(
                        expand=1,
                        content=ft.Container(
                                bgcolor="#FFF5E5",
                                
                                border_radius=ft.BorderRadius.all(10),
                                alignment=ft.Alignment.CENTER,
                                content= ft.Image(f"illustration/login.png"),padding=50),
                                )
                ],
                
            ),

            bgcolor=ft.Colors.SURFACE,
            border_radius=ft.BorderRadius.all(10),
            padding=ft.Padding.all(50),
            

        ),



        gradient=ft.LinearGradient(
            begin=ft.Alignment.BOTTOM_LEFT,
            end=ft.Alignment.TOP_RIGHT,
            colors=["#F7A31C", "#033C59"],
        ),

        expand=True,
        margin=ft.Margin.all(0),
        border_radius=ft.BorderRadius.all(10),
        padding=ft.Padding.symmetric(horizontal=200, vertical=50)

    )
    return login
