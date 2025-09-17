import flet as ft
from components.onboarding import previous, next


def on_product(page) -> ft.Control:


    product_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("📦", size=40),
            ft.Text("Ajoutez vos produits en un clic", size=40, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "Centralisez toutes vos références et " \
                "suivez vos quantités en temps réel.", size=22, font_family="PoppinsMedium", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.margin.symmetric(vertical=8)),
            ft.Row(
                controls=[
                    previous(page=page, route="/on_welcome"),
                    next(page=page, route="/on_sale")
                ],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.padding.only(right=20)

    )

    return product_container
