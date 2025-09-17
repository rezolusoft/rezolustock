import flet as ft
from components.onboarding import next


def on_start(page) -> ft.Control:


    start_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("🚀", size=40),
            ft.Text("Démarrer maintenant !", size=40, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "Configurer votre boutique et Ajoutez " \
                "vos premiers produits puis découvrez " \
                "tout ce que Akonta peut faire pour vous.", size=22, font_family="PoppinsMedium", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.margin.symmetric(vertical=8)),
            ft.Row(
                controls=[
                    next(page=page, route="/on_shop_register", name="Commencer")
                ],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.padding.only(right=20)

    )

    return start_container
