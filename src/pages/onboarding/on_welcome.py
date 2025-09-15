import flet as ft
from components.onboarding import next



def on_welcome(page) -> ft.Control:
    

    on_welcome = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("👋🏾", size=40),
            ft.Text("Bienvenu sur Akonta", size=40, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "La solution simple et efficace pensé" \
                " et conçu pour gérer vos stocks, vos " \
                "ventes et optimiser vos activités.", size=22, font_family="PoppinsMedium", color=ft.Colors.ON_SURFACE),
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

    return on_welcome
