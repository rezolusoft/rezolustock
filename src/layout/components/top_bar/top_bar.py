import flet as ft
from .search_bar import search_bar


def top_bar()->ft.Control:
    top_bar = ft.Container(
    bgcolor=ft.Colors.SURFACE,

    content=ft.Row(controls=[
        
        
        search_bar(), 


    ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

)

    top_bar.border_radius = ft.BorderRadius.all(10)
    
    return top_bar


