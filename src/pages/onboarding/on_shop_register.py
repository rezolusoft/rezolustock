import time
import flet as ft
from utils.tools import id_generator, local_file_uploader
from utils.validators import is_valid_email
from components.notification import rstocknotif
import asyncio
from pathlib import Path
from core.context.store import RStockStore




def on_shop_register(page) -> ft.Control:

    # CHAMPS DU FORMULAIRE D'ENREGISTREMENT D'UNE BOUTIQUE
    shop_name_field = ft.TextField(hint_text="*Nom boutique", border_radius=5, color=ft.Colors.PRIMARY, expand=1)

    email_field = ft.TextField(hint_text="*Email", border_radius=5, color=ft.Colors.PRIMARY, expand=1)

    phone_field = ft.TextField(hint_text="*Téléphone", border_radius=5, color=ft.Colors.PRIMARY, expand=1)

    adress_field = ft.TextField(hint_text="*Adresse boutique", border_radius=5, color=ft.Colors.PRIMARY, expand=1)

    rccm_field = ft.TextField(hint_text="RCCM", border_radius=5, color=ft.Colors.PRIMARY, expand=1)

    ifu_field = ft.TextField(hint_text="Numéro IFU", border_radius=5, color=ft.Colors.PRIMARY, expand=1)

    owner_firstname_field = ft.TextField(hint_text="*Prénoms du Propriétaire", border_radius=5, color=ft.Colors.PRIMARY, expand=1)

    owner_lastname_field = ft.TextField(hint_text="*Nom du Propriétaire",border_radius=5, color=ft.Colors.PRIMARY, expand=1)

    # CHAMPS DU FORMULAIRE D'ENREGISTREMENT D'UNE BOUTIQUE
    

    # FONCTION DE GESTION D'AJOUT DE FICHIER
    

    logo_file_state = {
        "file" : None,
        "error" : ft.Text("", color=ft.Colors.WHITE, size=12 )
    }

    async def on_logo_selected(e: ft.Event[ft.Button]):

        files = await ft.FilePicker().pick_files(allow_multiple=False, initial_directory=f"{Path.home()/"Pictures"}", file_type=ft.FilePickerFileType.IMAGE)
        if files:
            select_logo.content = f"Logo -> {files[0].name}"
            logo_file_state["file"] = files[0]
            select_logo.color = ft.Colors.SURFACE
            select_logo.style = ft.ButtonStyle(
                padding=ft.Padding.symmetric(vertical=15),
                bgcolor=ft.Colors.GREEN_600,
                shape=ft.RoundedRectangleBorder(radius=5),
            )
            page.update()

        

    # SELECTEUR DE FICHIER
    
    
    # BOUTON DECLENCHEUR DU SELECTEUR DE FICHIER
    select_logo = ft.Button(
        "Ajouter votre logo (Optionnel)",
        icon=ft.Icons.ARROW_CIRCLE_UP_OUTLINED,
        color=ft.Colors.SURFACE,
        expand=1,
        style=ft.ButtonStyle(
            padding=ft.Padding.symmetric(vertical=15),
            bgcolor=ft.Colors.PRIMARY,
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=on_logo_selected,
      )
    
 

    # FONCTION DE TRAITEMENT DE FORMULAIRE

    def form_is_valid():
        shop = {
            "name" : shop_name_field,
            "email" : email_field,
            "phone" : phone_field,
            "adress" : adress_field,
            "ifu" : ifu_field,
            "rccm" : rccm_field,
            "first_name" : owner_firstname_field,
            "last_name" : owner_lastname_field
        }

        # Validation du nom de boutique
        valid = True
        if not shop["name"].value.strip():
            shop["name"].error = "Veuillez renseigner le nom de votre boutique/commerce"
            valid = False
        else:
            shop["name"].error = None
            shop["name"].border_color = ft.Colors.GREEN_400
            valid = True

        # Validation de l'email de boutique
        if not shop["email"].value.strip():
            shop["email"].error = "Veuillez renseigner une adresse email valide"
            valid=False
        elif not is_valid_email(shop["email"].value.strip()):
            shop["email"].error = "Veuillez renseigner une adresse email valide"
            valid=False
        else:
            shop["email"].error = None
            shop["email"].border_color = ft.Colors.GREEN_400
            valid = True

        # Validation du numéro de téléphone de boutique
        if not shop["phone"].value.strip():
            shop["phone"].error = "Veuillez renseigner un numéro de téléphone"
            valid=False
        else:
            shop["phone"].error = None
            shop["phone"].border_color = ft.Colors.GREEN_400
            valid = True
        
        # Validation du l'adresse de la boutique
        if not shop["adress"].value.strip():
            shop["adress"].error = "Veuillez renseigner l'adresse de la boutique"
            valid=False
        else:
            shop["adress"].error = None
            shop["adress"].border_color = ft.Colors.GREEN_400
            valid = True
        
        # Validation du prénom du gérant de la boutique
        if not shop["first_name"].value.strip():
            shop["first_name"].error = "Veuillez renseigner votre Prénom"
            valid=False
        else:
            shop["first_name"].error = None
            shop["first_name"].border_color = ft.Colors.GREEN_400
            valid = True
        
        # Validation du nom du gérant de la boutique
        if not shop["last_name"].value.strip():
            shop["last_name"].error = "Veuillez renseigner votre Nom"
            valid=False
        else:
            shop["last_name"].error = None
            shop["last_name"].border_color = ft.Colors.GREEN_400
            valid=True

        if not logo_file_state["file"]:
            select_logo.content = "Ajoutez votre logo (optionnel)"
            select_logo.color = ft.Colors.SURFACE
            select_logo.style = ft.ButtonStyle(
                padding=ft.Padding.symmetric(vertical=15),
                bgcolor=ft.Colors.PRIMARY,
                shape=ft.RoundedRectangleBorder(radius=5),
            )
            valid=True
        else:
            logo_file_state["error"].value = None
            valid = True
        

        return valid


    async def form_handler():

        # RECUPERATION DES DONNEES ENTRER PAR L'UTILISATEUR

        if form_is_valid() :

            #Si aucun logo n'est selectionné, on met un logo par defaut
            if not logo_file_state["file"]:
                logo_dest = "assets/img/mini_logo.png"

            else:

                # RECUPERER ET UPLOADER LOGO
                logo_dest = local_file_uploader(logo_file_state["file"])
            
            # Recuperer les infos de la boutique
            shop = {
                "name": shop_name_field.value.strip(),
                "email": email_field.value.strip(),
                "phone": phone_field.value.strip(),
                "adress": adress_field.value.strip(),
                "ifu": ifu_field.value.strip(),
                "rccm": rccm_field.value.strip(),
                "first_name": owner_firstname_field.value.strip(),
                "last_name": owner_lastname_field.value.strip(),
                "logo": logo_dest
            }

            # ENREGISTRER INFOS BOUTIQUE ET ETAT
            store = RStockStore()
            await store.set_shop(shop)
            await store.set_onboarding_step("on_add_password")

            notif = rstocknotif("Opération réussie ✅", "Les informations de la boutique ont été ajoutées avec succès.", [])
            page.show_dialog(notif)
            await asyncio.sleep(3.5)
            page.pop_dialog()
            await page.push_route("/on_add_password")
        
        else:
            page.update()
        


    
    save_shop_info = ft.Button(
        "Enregistrer boutique",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            padding=ft.Padding.symmetric(vertical=15),
            bgcolor=ft.Colors.SECONDARY,
            text_style=ft.TextStyle(
                font_family="PoppinsMedium",
                size=15,
            )
        ),
        icon=ft.Icons.SAVE_AS_OUTLINED,
        color=ft.Colors.WHITE,
        expand=1,
        on_click=form_handler
        )

    shop_register_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Row([ft.Text("Enregistrez Votre Boutique", size=25, font_family="PoppinsBold",  color=ft.Colors.ON_SURFACE, )]),
            ft.Row([shop_name_field]),
            ft.Row([email_field, phone_field]),
            ft.Row([adress_field]),
            ft.Row([rccm_field, ifu_field]),
            ft.Row([owner_lastname_field, owner_firstname_field]),
            ft.Row([select_logo]),
            ft.Row([save_shop_info])
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
    ),
    padding=ft.Padding.only(right=18)

    )

    return shop_register_container
