import flet as ft
from extras.routes import push

def side_menu_button(title, icon, page=None, destination=None)->ft.Control:

    # Déterminer si ce bouton est actif
    is_active = (page.route == destination)

    # Couleurs
    default_bg = ft.Colors.TRANSPARENT
    hover_bg = ft.Colors.ORANGE_50
    active_bg = ft.Colors.ORANGE_100

    # On part avec la couleur active ou par défaut
    bg_color = active_bg if is_active else default_bg

    button = ft.Container(
                ft.Row(
                    controls=[
                        ft.Icon(icon=getattr(ft.Icons, icon), color=ft.Colors.PRIMARY, size=20),
                        ft.Text(title, color=ft.Colors.ON_SURFACE),
                    
                    ],
                  expand=True,  
                ),
                padding=ft.Padding.all(3),
                margin=ft.Margin.only(left=7),
                bgcolor=bg_color,
                on_click= lambda e : e.page.run_task(push, e.page, destination),
                border_radius=ft.BorderRadius.all(5),

                
            )
    
    def on_hover(e: ft.HoverEvent):
        if not is_active:  # On ne change pas si déjà actif
            button.bgcolor = hover_bg if e.data == "true" else default_bg
            button.update()

    button.on_hover = on_hover
    
    return button
