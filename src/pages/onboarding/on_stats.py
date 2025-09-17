import flet as ft
from components.onboarding import previous, next


def on_stats(page) -> ft.Control:


    stats_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("📊", size=40),
            ft.Text("Analysez vos performances", size=40, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "Prenez de meilleures décisions grâce à des rapports clairs et précis.", size=22, font_family="PoppinsMedium", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.margin.symmetric(vertical=8)),
            ft.Row(
                controls=[
                    previous(page=page, route="/on_sale"),
                    next(page=page, route="/on_start")
                ],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.padding.only(right=20)

    )

    return stats_container
