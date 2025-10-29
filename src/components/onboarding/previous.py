import flet as ft


def previous(page, route, name="Précédent"):
    
    return ft.ElevatedButton(
                      content=ft.Row(
                          [
                              ft.Icon(name=ft.Icons.ARROW_BACK_ROUNDED, color=ft.Colors.ON_SURFACE),
                              ft.Text(name)
                          ]
                      ), 
                      style=ft.ButtonStyle(
                          shape=ft.RoundedRectangleBorder(10),
                          padding=15,
                          bgcolor=ft.Colors.SECONDARY,
                          text_style=ft.TextStyle(
                              font_family="PoppinsMedium",
                              size=18
                          )
                          ),
                          color=ft.Colors.ON_SURFACE,
                        
                        on_click=lambda e:page.go(route),
                        
    )
