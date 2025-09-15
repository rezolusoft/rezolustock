import flet as ft


def on_shop_register(page) -> ft.Control:



    next_button = ft.Button(
                    content=ft.Row(
                          [   
                              ft.Text("Commencer"),
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
                        
                        on_click=lambda e:page.go("/on_shop_register"),
                        
                    )
    

    on_shop_register = ft.Container(ft.Column(
        expand=True,
        controls=[
            
            ft.Row(
                controls=[
                    next_button
                ],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.padding.only(right=20)

    )

    return on_shop_register
