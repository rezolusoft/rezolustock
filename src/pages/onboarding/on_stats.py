import flet as ft
from layout.components.onboarder import previous, next


def on_stats() -> ft.Control:


    stats_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("📊", size=40),
            ft.Text("Analysez vos performances", size=20, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "Prenez de meilleures décisions grâce à des rapports clairs et précis.", size=15, font_family="Poppins", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.Margin.symmetric(vertical=3)),
            ft.Row(
                controls=[
                    previous(route="/on_sale"),
                    next(route="/on_start")
                ],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.Padding.only(right=20)

    )

    return stats_container
