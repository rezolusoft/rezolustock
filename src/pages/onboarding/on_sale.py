import flet as ft


def on_sale(page) -> ft.Control:

    previous_button = ft.Button(
                      content=ft.Row(
                          [
                              ft.Icon(name=ft.Icons.ARROW_BACK_ROUNDED, color=ft.Colors.ON_SURFACE),
                              ft.Text("Précédent")
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
                        
                        on_click=lambda e:page.go("/on_stats"),
                        
                    )
    

    on_sale = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("💰", size=40),
            ft.Text("Gardez le contrôle sur vos transactions", size=40, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            ft.Text(
                "Enregistrez vos ventes, suivez vos marges et vos bénéfices.", size=22, font_family="PoppinsMedium", color=ft.Colors.ON_SURFACE),
            ft.Container(margin=ft.margin.symmetric(vertical=8)),
            ft.Row(
                controls=[
                    previous_button,
                    next_button
                ],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.padding.only(right=20)

    )

    return on_sale
