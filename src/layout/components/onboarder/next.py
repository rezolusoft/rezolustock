import flet as ft
from extras.routes import push


def next(route, name="Suivant"):
    
    return ft.Button(
                    content=ft.Row(
            controls=[
                ft.Text(name),
                    ft.Icon(ft.Icons.ARROW_FORWARD_ROUNDED, color=ft.Colors.WHITE,),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                
            ),
                    
                    bgcolor=ft.Colors.SECONDARY,
                      style=ft.ButtonStyle(
                          shape=ft.RoundedRectangleBorder(radius=5),
                          padding=10,
                          color=ft.Colors.WHITE,
                          
                          text_style=ft.TextStyle(
                              font_family="PoppinsMedium",
                              size=15,)
                          ),

                
                        
                        on_click=lambda e:e.page.run_task(push, e.page, route),
                        
                    )
