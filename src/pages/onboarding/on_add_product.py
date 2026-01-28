import flet as ft
import time
from models.product import Product
from models.category import Category
from pathlib import Path
from extras.store import RStockStore
from extras.tools import local_file_uploader
from components.rstocknotif import rstocknotif



def dropdown_categories():

    categories = Category.select().order_by(Category.name)
    categories_option = [ft.DropdownOption(key=category.id, text=category.name) for category in categories]
    return categories_option

def on_category_select(e):
    print(f"selected : {e.control.value}")


def on_add_product(page) -> ft.Control:

    store = RStockStore(page=page)

    product_name_field = ft.TextField(hint_text="*Nom Produit", border_radius=10)

    product_description_field = ft.TextField(hint_text="*Description Produit", multiline=True, min_lines=3, max_lines=3, border_radius=10)

    product_category_dropdown = ft.Dropdown(hint_text="Sélectionner une catégorie", options=dropdown_categories(), on_change=on_category_select, expand=True, border_radius=10)

    product_price_field = ft.TextField(hint_text="*Prix de vente", border_radius=10, expand=1,)
    
    product_cost_field = ft.TextField(hint_text="*Prix de revient", border_radius=10, expand=1)

    product_image_state = {
        "file" : None,
        "error" : ft.Text("", color=ft.Colors.ERROR, size=12)
    }
    def on_product_image_selected(e: ft.FilePickerResultEvent):

        if e.files:
            product_image.text = f"Image Produit -> {e.files[0].name}"
            product_image_state["file"] = e.files[0]
            product_image.color = ft.Colors.SURFACE
            product_image.style = ft.ButtonStyle(
                padding=ft.padding.symmetric(vertical=15),
                bgcolor=ft.Colors.GREEN_600,
                shape=ft.RoundedRectangleBorder(10),
            )

            page.update()


    product_image_picker = ft.FilePicker(on_result=on_product_image_selected)

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
    
    page.overlay.append(product_image_picker)
    page.update()


    def form_is_valid():
        product = {
            "name" : product_name_field,
            "description" : product_description_field,
            "category" : product_category_dropdown,
            "price" : product_price_field,
            "cost" : product_cost_field,
        }

        valid = True

        if not product["name"].value.strip():
            product["name"].error_text = "Veuillez renseigner un nom pour votre produit"
            valid = False
        else:
            product["name"].error_text = None
            product["name"].border_color = ft.Colors.GREEN_400
            valid = True
        if not product["category"].value:
            product["category"].error_text = "Veuillez choisir une catégorie pour votre produit"
            valid = False
        else:
            product["category"].error_text = None
            product["category"].border_color = ft.Colors.GREEN_400
            valid = True
        
        if not product["description"].value.strip():
            product["description"].error_text = "Veuillez renseigner une description pour votre produit"
            valid = False
        else:
            product["description"].error_text = None
            product["description"].border_color = ft.Colors.GREEN_400
            valid = True
        
        if not product["price"].value.strip():
            product["price"].error_text = "Veuillez renseigner un prix pour votre produit"
            valid = False
        else:
            product["price"].error_text = None
            product["price"].border_color = ft.Colors.GREEN_400
            valid = True
        
        if not product["cost"].value.strip():
            product["cost"].error_text = "Veuillez renseigner un prix de revient pour votre produit"
            valid = False
        else:
            product["cost"].error_text = None
            product["cost"].border_color = ft.Colors.GREEN_400
            valid = True
        
        if not product_image_state["file"]:
            product_image.text = "Vous devez ajouter un logo !"
            product_image.color = ft.Colors.RED_500
            product_image.style = ft.ButtonStyle(
                padding=ft.padding.symmetric(vertical=15),
                bgcolor=ft.Colors.PRIMARY,
                shape=ft.RoundedRectangleBorder(10),
            )
            valid=False
        else:
            product_image_state["error"].value = None
            valid = True
        
        return valid
    

    def form_handler(e):

        if form_is_valid():
            img_dest = local_file_uploader(product_image_state["file"])

            new_product = Product(
                name = product_name_field.value.strip(),
                description = product_description_field.value.strip(),
                category = product_category_dropdown.value.strip(),
                price = product_price_field.value.strip(),
                cost = product_cost_field.value.strip(),
                image = img_dest
            )

            new_product.save()

            notif = rstocknotif("Opération réussie ✅", "Votre premier produit produit à été ajoutée avec succès ! ", [])

            store.destroy("onboarding_step")
            store.set("onboarding_step", "on_done")

            page.open(notif)

            time.sleep(3)

            page.close(notif)

            page.go("/on_done")
        
        else:
            page.update()


    
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
        on_click=form_handler
        )



    

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

