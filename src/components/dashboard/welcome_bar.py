import flet as ft



def welcome_bar():


    rstock_date_picker = ft.SubmenuButton(
        content = ft.TextField(value="03/14/2026 - 03/20/2026", dense=True),
        key="smbutton",
        width=260,
        expand=True,
        menu_style=ft.MenuStyle(
            alignment=ft.Alignment.BOTTOM_CENTER, side=ft.BorderSide(1),

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
                border_radius=5,
                border=ft.Border.all(1)
            )
    
    return ft.Container(
        ft.Row([
            ft.Column([

                ft.Text("👋 Bonjour Abiodoun", color=ft.Colors.PRIMARY, font_family="PoppinsBold"),
                ft.Text("Quoi de neuf chez rezolusoft aujourd'hui ?", color=ft.Colors.PRIMARY, font_family="PoppinsMedium"),
                
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
        border_radius=5,
        padding=10,
        
    )
