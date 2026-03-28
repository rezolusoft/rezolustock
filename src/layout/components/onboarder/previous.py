import flet as ft
from extras.routes import push


def previous( route, name="Précédent"):
    
    return ft.ElevatedButton(
                      content=ft.Row(
                          [
                              ft.Icon(name=ft.Icons.ARROW_BACK_ROUNDED, color=ft.Colors.WHITE),
                              ft.Text(name)
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
                        
                        on_click=lambda e:e.page.run_task(push, e.page, route),
                        
    )
