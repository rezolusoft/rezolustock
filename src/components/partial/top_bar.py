import flet as ft
from .top_bar_title import top_bar_title
from .search_bar import search_bar
from .settings_menu import settings_menu


def top_bar()->ft.Control:
    top_bar = ft.Container(
    bgcolor=ft.Colors.SURFACE,

    content=ft.Row(controls=[
        
        top_bar_title('Dashboard', 'Bon retour sur Akonta'),
        
        search_bar(), 

        settings_menu()

    ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

)

    top_bar.border_radius = ft.border_radius.all(10)
    
    return top_bar


