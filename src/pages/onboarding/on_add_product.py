import flet as ft
import time
from models.product import Product
from models.category import Category
from pathlib import Path
from extras.store import RStockStore
from extras.tools import local_file_uploader
from components.rstocknotif import rstocknotif



def dropdown_categories():
    categories = Category.select()
    categories_option = [ft.DropdownOption(key=category.id, text=category.name) for category in categories]
    return categories_option

def on_add_product(page) -> ft.Control:
    product_name_field = ft.TextField(hint_text="*Nom Produit", border_radius=10)

    product_description_field = ft.TextField(hint_text="*Description Produit", multiline=True, min_lines=3, max_lines=3, border_radius=10)

    product_category_dropdown = ft.Dropdown(hint_text="Sélectionner une catégorie", options=dropdown_categories(), expand=True, border_radius=10)

    product_price_field = ft.TextField(hint_text="*Prix de vente", border_radius=10, expand=1)
    
    product_cost_field = ft.TextField(hint_text="*Prix de revient", border_radius=10, expand=1)

    product_image_picker = ft.FilePicker(on_result="")

    product_image = ft.ElevatedButton(
        "Ajouter image produit",
        icon=ft.Icons.ARROW_CIRCLE_UP_OUTLINED,
        color=ft.Colors.SURFACE,
        expand=1,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(vertical=15),
            bgcolor=ft.Colors.PRIMARY,
            shape=ft.RoundedRectangleBorder(10),
        ),
        on_click=lambda _: product_image_picker.pick_files(allow_multiple=False, initial_directory=Path.home()/"Pictures", file_type=ft.FilePickerFileType.IMAGE),
      )
    
    save_product = ft.ElevatedButton(
        "Enregistrer Produit",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(10),
            padding=ft.padding.symmetric(vertical=15),
            bgcolor=ft.Colors.SECONDARY,
            text_style=ft.TextStyle(
                font_family="PoppinsMedium",
                size=16
            )
        ),
        icon=ft.Icons.SAVE_AS_OUTLINED,
        color=ft.Colors.ON_SURFACE, 
        expand=1,
        )



    store = RStockStore(page=page)

    add_product_container = ft.Column(
        controls=[
            ft.Container(
                ft.Column(
                    expand=True,
                    controls=[
                        
                            ft.Row([ft.Text("Ajouter Un Premier Produit", size=25, font_family="PoppinsBold",  color=ft.Colors.ON_SURFACE)]),
                            product_name_field,
                            product_category_dropdown,
                            product_description_field,
                            ft.Row([product_cost_field, product_price_field]),
                            ft.Row([product_image]),
                            ft.Row([save_product])

                    ],
                    spacing=20,
                ),
                padding=ft.padding.only(right=18)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    return add_product_container

