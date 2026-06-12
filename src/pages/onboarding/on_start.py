import flet as ft
from layout.components.onboarder import next


def on_start() -> ft.Control:


    start_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("🚀", size=40),
            ft.Text("Démarrez maintenant !", size=20, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "Configurez votre boutique et Ajoutez " \
                "vos premiers produits puis découvrez " \
                "tout ce que RezoluStock peut faire pour vous.", size=15, font_family="Poppins", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.Margin.symmetric(vertical=3)),
            ft.Row(
                controls=[
                    next(route="/on_shop_register", name="Commencer")
                ],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.Padding.only(right=20)

    )

    return start_container
