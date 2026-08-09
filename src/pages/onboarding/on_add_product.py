import flet as ft
import time
from models.product import Product
from models.category import Category
from pathlib import Path
import asyncio
from core.context.store import RStockStore
from utils.tools import local_file_uploader
from components.notification import rstocknotif



def dropdown_categories():

    categories = Category.select().order_by(Category.name)
    categories_option = [ft.DropdownOption(key=category.id, text=category.name) for category in categories]
    return categories_option

def on_category_select(e):
    print(f"selected : {e.control.value}")


def on_add_product(page) -> ft.Control:

    store = RStockStore()

    product_name_field = ft.TextField(hint_text="*Nom Produit", border_radius=10, expand=1)

    product_description_field = ft.TextField(hint_text="*Description Produit", multiline=True, min_lines=3, max_lines=3, border_radius=10, expand=1)

    product_category_dropdown = ft.Dropdown(hint_text="Sélectionnez une catégorie", options=dropdown_categories(), on_select=on_category_select, expand=True, border_radius=10)

    product_price_field = ft.TextField(hint_text="*Prix de vente", border_radius=10, expand=1, keyboard_type=ft.KeyboardType.NUMBER, input_filter=ft.InputFilter(allow=True, regex_string="[0-9]*\.?[0-9]*"))
    
    product_cost_field = ft.TextField(hint_text="*Prix de revient", border_radius=10, expand=1, keyboard_type=ft.KeyboardType.NUMBER, input_filter=ft.InputFilter(allow=True, regex_string="[0-9]*\.?[0-9]*"))

    product_quantity_field = ft.TextField(hint_text="*Quantité", border_radius=10, expand=1, keyboard_type=ft.KeyboardType.NUMBER, input_filter=ft.InputFilter(allow=True, regex_string="[0-9]*"))
    product_quantity_alert_field = ft.TextField(hint_text="*Seuil Critique stock", border_radius=10, expand=1, keyboard_type=ft.KeyboardType.NUMBER, input_filter=ft.InputFilter(allow=True, regex_string="[0-9]*"))


    product_image_state = {
        "file" : None,
        "error" : ft.Text("", color=ft.Colors.ERROR, size=12)
    }
    async def on_product_image_selected(e: ft.Event[ft.Button]):

        files = await ft.FilePicker().pick_files(allow_multiple=False, initial_directory=f"{Path.home()/"Pictures"}", file_type=ft.FilePickerFileType.IMAGE)
        if files:
            product_image.content = f"Image Produit -> {files[0].name}"
            product_image_state["file"] = files[0]
            product_image.color = ft.Colors.SURFACE
            product_image.style = ft.ButtonStyle(
                padding=ft.Padding.symmetric(vertical=15),
                bgcolor=ft.Colors.GREEN_600,
                shape=ft.RoundedRectangleBorder(radius=10),
            )

            page.update()



    product_image = ft.Button(
        "Ajouter image produit",
        icon=ft.Icons.ARROW_CIRCLE_UP_OUTLINED,
        color=ft.Colors.SURFACE,
        expand=1,
        style=ft.ButtonStyle(
            padding=ft.Padding.symmetric(vertical=15),
            bgcolor=ft.Colors.PRIMARY,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        on_click= on_product_image_selected
      )
    
 
    page.update()


    def form_is_valid():
        product = {
            "name" : product_name_field,
            "description" : product_description_field,
            "category" : product_category_dropdown,
            "price" : product_price_field,
            "cost" : product_cost_field,
            "quantity" : product_quantity_field,
            "quantity_alert" : product_quantity_alert_field
        }

        valid = True

        #Traitement des champs texte
        if not product["name"].value.strip():
            product["name"].error = "Veuillez renseigner un nom pour votre produit"
            valid = False
        else:
            product["name"].error = None
            product["name"].border_color = ft.Colors.GREEN_400
            valid = True
        if not product["category"].value:
            product["category"].error = "Veuillez choisir une catégorie pour votre produit"
            valid = False
        else:
            product["category"].error = None
            product["category"].border_color = ft.Colors.GREEN_400
            valid = True
        
        if not product["description"].value.strip():
            product["description"].error = "Veuillez renseigner une description pour votre produit"
            valid = False
        else:
            product["description"].error = None
            product["description"].border_color = ft.Colors.GREEN_400
            valid = True

        #Traitement des champs numériques
        qty = (product["quantity"].value or "").strip()
        try:
            qty = float(qty) if qty else -1
        except ValueError:
            qty = -1
        if qty < 0:
            product["price"].error = "Veuillez renseigner un prix pour votre produit"
            valid = False
        else:
            product["price"].error = None
            product["price"].border_color = ft.Colors.GREEN_400
            valid = True
        
        qty1 = (product["cost"].value or "").strip()
        try:
            qty1 = float(qty1) if qty1 else -1
        except ValueError:
            qty1 = -1
        if qty1 < 0:
            product["cost"].error = "Veuillez renseigner un prix de revient pour votre produit"
            valid = False
        else:
            product["cost"].error = None
            product["cost"].border_color = ft.Colors.GREEN_400
            valid = True

        qty2 = (product["quantity"].value or "").strip()
        try:
            qty2 = int(qty2) if qty2 else -1
        except ValueError:
            qty2 = -1
        if qty2 < 0:
            product["quantity"].error = "Veuillez rensiegner une quantité de produit"
            valid=False
        else:
            product["quantity"].error = None
            product["quantity"].border_color = ft.Colors.GREEN_400
            valid = True
        
        qty3 = (product["quantity_alert"].value or "").strip()
        try:
            qty3 = int(qty3) if qty3 else -1
        except ValueError:
            qty3 = -1
        if qty3 < 0:
            product["quantity_alert"].error = "Veuillez rensiegner une seuil de stock"
            valid=False
        else:
            product["quantity_alert"].error = None
            product["quantity_alert"].border_color = ft.Colors.GREEN_400
            valid = True
    
        if not product_image_state["file"]:
            product_image.content = "Vous devez ajouter un logo !"
            product_image.color = ft.Colors.RED_500
            product_image.style = ft.ButtonStyle(
                padding=ft.Padding.symmetric(vertical=15),
                bgcolor=ft.Colors.PRIMARY,
                shape=ft.RoundedRectangleBorder(radius=10),
            )
            valid=False
        else:
            product_image_state["error"].value = None
            valid = True
        
        return valid
    

    async def form_handler(e):

        if form_is_valid():
            img_dest = local_file_uploader(product_image_state["file"])

            new_product = Product(
                name = product_name_field.value.strip(),
                description = product_description_field.value.strip(),
                category = product_category_dropdown.value.strip(),
                price = product_price_field.value.strip(),
                cost = product_cost_field.value.strip(),
                image = img_dest,
                quantity = product_quantity_field.value.strip(),
                quantity_alert = product_quantity_alert_field.value.strip()
            )

            new_product.save()

            notif = rstocknotif("Opération réussie ✅", "Votre premier produit produit à été ajoutée avec succès ! ", [])

            await store.set_onboarding_step("on_done")

            page.show_dialog(notif)

            await asyncio.sleep(3.5)

            page.pop_dialog()

            await page.push_route("/on_done")
        
        else:
            page.update()


    
    save_product = ft.Button(
        "Enregistrer Produit",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.Padding.symmetric(vertical=15),
            bgcolor=ft.Colors.SECONDARY,
            text_style=ft.TextStyle(
                font_family="PoppinsMedium",
            )
        ),
        icon=ft.Icons.SAVE_AS_OUTLINED,
        color=ft.Colors.WHITE, 
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
                            ft.Row([product_quantity_field, product_quantity_alert_field]),
                            ft.Row([product_image]),
                            ft.Row([save_product])

                    ],
                    spacing=20,
                ),
                padding=ft.Padding.only(right=18)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    return add_product_container

