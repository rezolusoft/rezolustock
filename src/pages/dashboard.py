import flet as ft

def dashboard()->ft.Control:
    dashboard = ft.Container(ft.Row(
    expand=True,
    controls=[
        ft.Text("hello")
    ],
    ),
    bgcolor=ft.Colors.SURFACE,
    )
    dashboard.border_radius = ft.BorderRadius.all(5)
    return dashboard
