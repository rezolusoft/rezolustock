import flet as ft


def sale_item(img:str|None, name:str|None, price:int|None, sale:int|None):
    return ft.Container(
        ft.Row(
            [
                ft.Container(ft.Image(img, width=80)),

                ft.Container(ft.Column(
                    [
                        ft.Text(name, font_family="PoppinsSemiBold", color=ft.Colors.PRIMARY),
                        ft.Row([
                            ft.Text(f"{price} XOF", color=ft.Colors.PRIMARY),
                            ft.Text(f"{sale} Ventes", color=ft.Colors.PRIMARY),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        expand=True
                        )
                    ]
                ),
                  expand=True
                )

            ],
            expand=True
        ),
        expand=True
    )


def top_sales():

    return ft.Container(

        ft.Column(
            [
                ft.Text("Les plus vendu", font_family="PoppinsBold", color=ft.Colors.PRIMARY),
                ft.Divider(ft.Colors.PRIMARY),
                sale_item("icon.png", "Sauce legume Mega", 250000, 1520),
                sale_item("icon.png", "Sauce legume Mega", 250000, 1520),
                sale_item("icon.png", "Sauce legume Mega", 250000, 1520),
                sale_item("icon.png", "Sauce legume Mega", 250000, 1520),
                sale_item("icon.png", "Sauce legume Mega", 250000, 1520),
       
            ]
        ),

        bgcolor=ft.Colors.SURFACE,
        expand=2,
        padding=10,
        border_radius=10

    )

