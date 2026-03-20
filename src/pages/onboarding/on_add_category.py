import flet as ft
import time
from models.category import Category
from pathlib import Path
from extras.store import RStockStore
from extras.tools import local_file_uploader
from components.rstocknotif import rstocknotif




def on_add_category(page) -> ft.Control:

    store = RStockStore(page=page)

    category_name_field = ft.TextField(hint_text="*Nom Catégorie", border_radius=10)
    category_description_field = ft.TextField(hint_text="*Description Catégorie", multiline=True, min_lines=3, max_lines=3, border_radius=10)
    
    category_image_state = {
        "file" : None,
        "error" : ft.Text("", color=ft.Colors.ERROR, size=12)
    }

    def on_category_image_selected(e: ft.FilePickerResultEvent):
        
        if e.files:
            category_image.text = f"Image Catégorie -> {e.files[0].name}"
            category_image_state["file"] = e.files[0]
            category_image.color = ft.Colors.SURFACE
            category_image.style = ft.ButtonStyle(
                padding=ft.padding.symmetric(vertical=15),
                bgcolor=ft.Colors.GREEN_600,
                shape=ft.RoundedRectangleBorder(10),
            )
            page.update()
             
    
    category_image_dialog = ft.FilePicker(on_result = on_category_image_selected)



    category_image = ft.ElevatedButton(
        "Ajouter une image descriptive",
        icon = ft.Icons.ARROW_CIRCLE_UP_OUTLINED,
        color = ft.Colors.SURFACE,
        expand=1,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(vertical=15),
            bgcolor=ft.Colors.PRIMARY,
            shape=ft.RoundedRectangleBorder(10),
        ),
        on_click=lambda _: category_image_dialog.pick_files(allow_multiple=False, initial_directory=Path.home()/"Pictures", file_type=ft.FilePickerFileType.IMAGE),
    )

    page.overlay.append(category_image_dialog)
    page.update()

    def form_is_valid():
        category = {
            "name": category_name_field,
            "description": category_description_field
        }

        valid = True
        if not category["name"].value.strip():
            category["name"].error_text = "Veuillez renseigner le nom de votre catégorie produit"
            valid = False
        else:
            category["name"].error_text = None
            category["name"].border_color = ft.Colors.GREEN_400
            valid = True
        
        if not category["description"].value.strip():
            category["description"].error_text = "Veuillez renseigner le nom de votre catégorie produit"
            valid = False
        else:
            category["description"].error_text = None
            valid = True
        
        
        return valid
    
    def form_handler(e) :
        if form_is_valid():
            image_dest = local_file_uploader(category_image_state["file"])
            
            new_category = Category(
                name = category_name_field.value.strip(),
                description = category_description_field.value.strip(),
                image = image_dest
            )
            new_category.save()

            notif = rstocknotif("Opération réussie ✅", "Votre première catégorie produit à été ajoutée avec succès ! ", [])

            store.destroy("onboarding_step")
            store.set("onboarding_step", "on_add_product")

            page.open(notif)
            time.sleep(3)
            page.close(notif)
            page.go("/on_add_product")
        
        else:
            page.update()
    
    save_category = ft.ElevatedButton(
        "Enregistrer Category",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(10),
            padding=ft.padding.symmetric(vertical=15),
            bgcolor=ft.Colors.SECONDARY,
            text_style=ft.TextStyle(
                font_family="PoppinsMedium",
            )
        ),
        icon=ft.Icons.FOLDER_OUTLINED,
        color=ft.Colors.WHITE, 
        expand=1,
        on_click=form_handler
        
        )
    add_category_container = ft.Column(
        controls=[
            ft.Container(
                ft.Column(
            
                    controls=[
                        
                            ft.Row([ft.Text("Ajouter Une Catégorie Produit", size=25, font_family="PoppinsBold",  color=ft.Colors.ON_SURFACE)]),
                            category_name_field,
                            category_description_field,
                            ft.Row(controls=[category_image], expand=True),
                            ft.Row(controls=[save_category], expand=True)

                    ],
                    spacing=20,
                ),
                padding=ft.padding.only(right=18)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    return add_category_container

