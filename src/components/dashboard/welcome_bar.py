import flet as ft
from core.context.state import RstockState



def welcome_bar(page):


    rstock_date_picker = ft.SubmenuButton(
        content = ft.TextField(value="03/14/2026 - 03/20/2026", dense=True),
        key="smbutton",
        width=260,
        expand=True,
        menu_style=ft.MenuStyle(
            alignment=ft.Alignment.BOTTOM_LEFT, 
            bgcolor=ft.Colors.WHITE,

        ),
        style=ft.ButtonStyle(
        overlay_color="transparent",  
        ),
        controls=[
            ft.MenuItemButton(
            content=ft.Text("Aujourd'hui"),
            on_click=lambda e: print(f"{e.control.content.value}.on_click"),
             ),

            ft.MenuItemButton(
            content=ft.Text("Hier"),
            on_click=lambda e: print(f"{e.control.content.value}.on_click"),
             ),
            
            ft.MenuItemButton(
            content=ft.Text("7 derniers jours"),
            on_click=lambda e: print(f"{e.control.content.value}.on_click"),
             ),
            
            ft.MenuItemButton(
            content=ft.Text("30 derniers jours"),
            on_click=lambda e: print(f"{e.control.content.value}.on_click"),
             ),
            
            ft.MenuItemButton(
            content=ft.Text("Dernier mois"),
            on_click=lambda e: print(f"{e.control.content.value}.on_click"),
             ),
            
            ft.MenuItemButton(
            content=ft.Text("Définir une période"),
            on_click=lambda e: print(f"{e.control.content.value}.on_click"),
             ),
        ]
    )


    

    reload = ft.Container(
                content=ft.Icon(ft.Icons.REPLAY_OUTLINED, color=ft.Colors.PRIMARY),
                padding=5,
                border_radius=10,
                border=ft.Border.all(1)
            )


    state = RstockState(page)
    user = state.get_current_user()

    return ft.Container(
        ft.Row([
            ft.Column([

                ft.Text(f"👋 Bonjour {user.first_name}", color=ft.Colors.PRIMARY, font_family="PoppinsBold"),
                ft.Text(f"Quoi de neuf chez {user.shop_name} aujourd'hui ?", color=ft.Colors.PRIMARY, font_family="PoppinsMedium"),
                
                ]
            ),

            ft.Row(
                [
                    rstock_date_picker,
                    reload
                ]
            )

        ],
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        bgcolor=ft.Colors.SURFACE,
        border_radius=10,
        padding=10,
        
    )
