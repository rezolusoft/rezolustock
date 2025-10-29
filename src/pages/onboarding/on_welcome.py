import flet as ft
from components.onboarding import next



def on_welcome(page) -> ft.Control:
    

    welcome_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("👋🏾", size=40),
            ft.Text("Bienvenue sur RezoluStock", size=25, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "La solution simple et efficace pensé" \
                " et conçu pour gérer vos stocks, vos " \
                "ventes et optimiser vos activités.", size=20, font_family="Poppins", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.margin.symmetric(vertical=8)),
            ft.Row(
                controls=[
                    next(page=page, route='/on_product')
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.padding.only(right=20)

    )

    return welcome_container
