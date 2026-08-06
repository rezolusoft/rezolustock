import flet as ft
from layout.components.onboarder import previous, next


def on_sale(page) -> ft.Control:

    sale_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("💰", size=40),
            ft.Text("Gardez le contrôle sur vos transactions", size=20, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "Enregistrez vos ventes, suivez vos marges et vos bénéfices.", size=16, font_family="Poppins", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.Margin.symmetric(vertical=3)),
            ft.Row(
                controls=[
                    previous(route="/on_product"),
                    next(route="/on_stats")
                ],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.Padding.only(right=20)

    )

    return sale_container
