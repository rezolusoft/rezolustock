import flet as ft
from extras.routes import push


def previous(route, name="Précédent"):
    
    return ft.Button(
                      content=name,
                      icon=ft.Icons.ARROW_BACK_ROUNDED,
                      icon_color=ft.Colors.WHITE,
                      color=ft.Colors.WHITE,
                      bgcolor=ft.Colors.SECONDARY,
                      style=ft.ButtonStyle(
                          shape=ft.RoundedRectangleBorder(radius=5),
                          padding=10,
                          text_style=ft.TextStyle(
                              font_family="PoppinsMedium",
                              size=15,
                              
                          )
                          ),
                          
                        
                        on_click=lambda e:e.page.run_task(push, e.page, route),
                        
    )
