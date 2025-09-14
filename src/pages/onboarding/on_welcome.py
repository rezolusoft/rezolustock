import flet as ft


def on_welcome(page) -> ft.Control:

    next_button = ft.Button(
                    content=ft.Row(
                          [   
                              ft.Text("Suivant"),
                              ft.Icon(name=ft.Icons.ARROW_FORWARD_ROUNDED, color=ft.Colors.ON_SURFACE),
                              
                          ]
                    ), 
                      style=ft.ButtonStyle(
                          shape=ft.RoundedRectangleBorder(10),
                          padding=15,
                          bgcolor=ft.Colors.SECONDARY,
                          text_style=ft.TextStyle(
                              font_family="PoppinsBold",
                              size=22
                          )
                          ),
                          color=ft.Colors.ON_SURFACE,
                        
                        on_click=lambda e:page.go("/on_product"),
                        
                    )
    

    on_welcome = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("👋🏾", size=40),
            ft.Text("Bienvenu sur Akonta", size=40, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "La solution simple et efficace pensé" \
                " et conçu pour gérer vos stocks, vos " \
                "ventes et optimiser vos activités.", size=22, font_family="PoppinsMedium", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.margin.symmetric(vertical=8)),
            ft.Row(
                controls=[
                    next_button
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.padding.only(right=20)

    )

    return on_welcome
