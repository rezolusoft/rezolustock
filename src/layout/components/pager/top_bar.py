import flet as ft

def search_bar() -> ft.Control:

    search_bar = ft.Container(ft.TextField(hint_text="Rechercher...", prefix_icon=ft.Icons.SEARCH_OUTLINED, dense=True, text_size=14, width=200,))
    search_bar.margin = ft.Margin.symmetric(horizontal=10)

    return search_bar


def top_bar()->ft.Control:
    top_bar = ft.Container(
    bgcolor=ft.Colors.SURFACE,

    content=ft.Row(controls=[
        
        
        search_bar(), 


    ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

)

    top_bar.border_radius = ft.BorderRadius.all(5)
    top_bar.padding = ft.Padding.all(10)
    
    return top_bar


