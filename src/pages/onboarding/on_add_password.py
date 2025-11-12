import flet as ft

def on_add_password(page) -> ft.Control:

    add_password_container = ft.Container(
        ft.Column(
            expand=True,
            controls=[
                ft.Text("DÉFINIR MOT DE PASSE")
            ]
        )
    )

    return add_password_container

