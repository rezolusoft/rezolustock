import flet as ft

def category(page)->ft.Control :

    category = ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text("Catégories"),
                                        ft.Text("Gérez vos catégories ici")
                                    ]
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        bgcolor=ft.Colors.SURFACE,
                        border_radius=10,
                    )
                ]
            )
        )
    
    return category
