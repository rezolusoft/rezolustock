import flet as ft
from layout.components.onboarder import next



def on_welcome() -> ft.Control:
    

    welcome_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("👋🏾", size=40),
            ft.Text("Bienvenue sur RezoluStock", size=20, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "La solution simple et efficace pensée" \
                " et conçue pour gérer vos stocks, vos " \
                "ventes et optimiser vos activités.", size=15, font_family="Poppins", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.Margin.symmetric(vertical=3)),
            ft.Row(
                controls=[
                    next(route='/on_product')
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.Padding.only(right=20)

    )

    return welcome_container
