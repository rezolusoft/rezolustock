import flet as ft
import time
from extras.store import RStockStore
from components.rstocknotif import rstocknotif




def on_add_category(page) -> ft.Control:

    store = RStockStore(page=page)

    
    save_shop_info = ft.ElevatedButton(
        "Enregistrer Mot de Passe",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(10),
            padding=ft.padding.symmetric(vertical=15),
            bgcolor=ft.Colors.SECONDARY,
            text_style=ft.TextStyle(
                font_family="PoppinsMedium",
                size=16
            )
        ),
        icon=ft.Icons.FOLDER_OUTLINED,
        color=ft.Colors.ON_SURFACE, 
        expand=1,
        )
    add_category_container = ft.Column(
        controls=[
            ft.Container(
                ft.Column(
            
                    controls=[
                        
                            ft.Row([ft.Text("Ajouter Une Catégorie Produit", size=25, font_family="PoppinsBold",  color=ft.Colors.ON_SURFACE)]),
                           
                            ft.Row(controls=[save_shop_info], expand=True)

                    ],
                    spacing=20,
                ),
                padding=ft.padding.only(right=18)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    return add_category_container

