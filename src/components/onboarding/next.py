import flet as ft


def next(page, route, name="Suivant"):
    
    return ft.Button(
                    content=ft.Row(
                          [   
                              ft.Text(name),
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
                        
                        on_click=lambda e:page.go(route),
                        
                    )
