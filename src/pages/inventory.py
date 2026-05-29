import flet as ft

def inventory()->ft.Control :
    inventory = ft.Container(content=ft.Text("Inventory -> Contenu Principal"), bgcolor=ft.Colors.SURFACE)
    return inventory
