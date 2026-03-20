import flet as ft


def next(page, route, name="Suivant"):
    
    return ft.ElevatedButton(
                    content=ft.Row(
                          [   
                              ft.Text(name),
                              ft.Icon(name=ft.Icons.ARROW_FORWARD_ROUNDED, color=ft.Colors.WHITE),
                              
                          ]
                    ), 
                      style=ft.ButtonStyle(
                          shape=ft.RoundedRectangleBorder(5),
                          padding=10,
                          bgcolor=ft.Colors.SECONDARY,
                          text_style=ft.TextStyle(
                              font_family="PoppinsMedium",
                              size=15
                          )
                          ),
                          color=ft.Colors.WHITE,
                        
                        on_click=lambda e:page.go(route),
                        
                    )
