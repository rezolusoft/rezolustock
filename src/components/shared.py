import flet as ft


def new_button():
    return ft.TextButton(content="Nouveau", style=ft.ButtonStyle(bgcolor=ft.Colors.SECONDARY, color=ft.Colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10), padding=10, text_style=ft.TextStyle(font_family="PoppinsSemiBold")), icon=ft.Icons.ADD_CIRCLE_OUTLINE_OUTLINED)


def export_to_pdf():
    return ft.Container(
                    content=ft.Image("img/pdf.png", width=22),
                    bgcolor=ft.Colors.SURFACE,
                    padding=5,
                    border_radius=10,
                )


def export_to_xls():
    return ft.Container(
                    content=ft.Image("img/xls.png", width=22),
                    bgcolor=ft.Colors.SURFACE,
                    padding=5,
                    border_radius=10,
                )
