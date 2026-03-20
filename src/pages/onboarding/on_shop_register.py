import time
import flet as ft
from extras.tools import is_valid_email, id_generator, local_file_uploader
from components.rstocknotif import rstocknotif
from pathlib import Path
from extras.store import RStockStore




def on_shop_register(page) -> ft.Control:

    # CHAMPS DU FORMULAIRE D'ENREGISTREMENT D'UNE BOUTIQUE
    shop_name_field = ft.TextField(hint_text="*Nom boutique", border_radius=5)

    email_field = ft.TextField(hint_text="*Email", border_radius=5, expand=1)

    phone_field = ft.TextField(hint_text="*Téléphone", border_radius=5, expand=1)

    adress_field = ft.TextField(hint_text="*Adresse boutique", border_radius=5)

    rccm_field = ft.TextField(hint_text="RCCM", border_radius=5, expand=1)

    ifu_field = ft.TextField(hint_text="Numéro IFU", border_radius=5, expand=1)

    owner_firstname_field = ft.TextField(hint_text="*Prénoms du Propriétaire",border_radius=5, expand=1)

    owner_lastname_field = ft.TextField(hint_text="*Nom du Propriétaire",border_radius=5, expand=1)

    # CHAMPS DU FORMULAIRE D'ENREGISTREMENT D'UNE BOUTIQUE
    

    # FONCTION DE GESTION D'AJOUT DE FICHIER
    

    logo_file_state = {
        "file" : None,
        "error" : ft.Text("", color=ft.Colors.WHITE, size=12 )
    }

    def on_logo_selected(e: ft.FilePickerResultEvent):
        if e.files:
            select_logo.text = f"Logo -> {e.files[0].name}"
            logo_file_state["file"] = e.files[0]
            select_logo.color = ft.Colors.SURFACE
            select_logo.style = ft.ButtonStyle(
                padding=ft.padding.symmetric(vertical=15),
                bgcolor=ft.Colors.GREEN_600,
                shape=ft.RoundedRectangleBorder(10),
            )
            page.update()


        else:
            select_logo.text = "Vous devez ajouter un logo !"
            select_logo.color = ft.Colors.WHITE
            select_logo.style = ft.ButtonStyle(
                padding=ft.padding.symmetric(vertical=15),
                bgcolor=ft.Colors.RED_600,
                shape=ft.RoundedRectangleBorder(10),
            )
            page.update()
        

    # SELECTEUR DE FICHIER
    select_logo_dialog = ft.FilePicker(on_result=on_logo_selected)
    
    
    # BOUTON DECLENCHEUR DU SELECTEUR DE FICHIER
    select_logo = ft.ElevatedButton(
        "Ajouter votre logo",
        icon=ft.Icons.ARROW_CIRCLE_UP_OUTLINED,
        color=ft.Colors.SURFACE,
        expand=1,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(vertical=15),
            bgcolor=ft.Colors.PRIMARY,
            shape=ft.RoundedRectangleBorder(5),
        ),
        on_click=lambda _: select_logo_dialog.pick_files(allow_multiple=False, initial_directory=Path.home()/"Pictures", file_type=ft.FilePickerFileType.IMAGE),
      )
    
    # AJOUT DU SELECTEUR DE FICHIER A LA PAGE
    page.overlay.append(select_logo_dialog)
    page.update()


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
            shop["name"].error_text = "Veuillez renseigner le nom de votre boutique/commerce"
            valid = False
        else:
            shop["name"].error_text = None
            shop["name"].border_color = ft.Colors.GREEN_400
            valid = True

        # Validation de l'email de boutique
        if not shop["email"].value.strip():
            shop["email"].error_text = "Veuillez renseigner une adresse email valide"
            valid=False
        elif not is_valid_email(shop["email"].value.strip()):
            shop["email"].error_text = "Veuillez renseigner une adresse email valide"
            valid=False
        else:
            shop["email"].error_text = None
            shop["email"].border_color = ft.Colors.GREEN_400
            valid = True

        # Validation du numéro de téléphone de boutique
        if not shop["phone"].value.strip():
            shop["phone"].error_text = "Veuillez renseigner un numéro de téléphone"
            valid=False
        else:
            shop["phone"].error_text = None
            shop["phone"].border_color = ft.Colors.GREEN_400
            valid = True
        
        # Validation du l'adresse de la boutique
        if not shop["adress"].value.strip():
            shop["adress"].error_text = "Veuillez renseigner l'adresse de la boutique"
            valid=False
        else:
            shop["adress"].error_text = None
            shop["adress"].border_color = ft.Colors.GREEN_400
            valid = True
        
        # Validation du prénom du gérant de la boutique
        if not shop["first_name"].value.strip():
            shop["first_name"].error_text = "Veuillez renseigner votre Prénom"
            valid=False
        else:
            shop["first_name"].error_text = None
            shop["first_name"].border_color = ft.Colors.GREEN_400
            valid = True
        
        # Validation du nom du gérant de la boutique
        if not shop["last_name"].value.strip():
            shop["last_name"].error_text = "Veuillez renseigner votre Nom"
            valid=False
        else:
            shop["last_name"].error_text = None
            shop["last_name"].border_color = ft.Colors.GREEN_400
            valid=True

        if not logo_file_state["file"]:
            select_logo.text = "Vous devez ajouter un logo !"
            select_logo.color = ft.Colors.RED_500
            select_logo.style = ft.ButtonStyle(
                padding=ft.padding.symmetric(vertical=15),
                bgcolor=ft.Colors.PRIMARY,
                shape=ft.RoundedRectangleBorder(10),
            )
            valid=False
        else:
            logo_file_state["error"].value = None
            valid = True

        return valid


    def form_handler(e):

        # RECUPERATION DES DONNEES ENTRER PAR L'UTILISATEUR

        if form_is_valid() :
            # RECUPERER LOGO
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
            store = RStockStore(page=page)
            shop_infos = store.check("shop_infos")
            if shop_infos:
                store.destroy("shop_infos")
                store.set("shop_infos", shop)
            else:
                store.set("shop_infos", shop)
            
            onboarding_step = store.check("onboarding_step")
            if onboarding_step:
                store.destroy("onboarding_step")
                store.set("onboarding_step", "on_add_password")
            else:    
                store.set("onboarding_step", "on_add_password")

            notif = rstocknotif("Opération réussie ✅", "Les informations de la boutique ont été ajoutées avec succès.", [])
            page.open(notif)
            time.sleep(3.5)
            page.close(notif)
            page.go("/on_add_password")
        
        else:
            page.update()
        


    
    save_shop_info = ft.ElevatedButton(
        "Enregistrer boutique",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(10),
            padding=ft.padding.symmetric(vertical=15),
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
            ft.Row([ft.Text("Enregistrer Votre Boutique", size=25, font_family="PoppinsBold",  color=ft.Colors.ON_SURFACE, )]),
            shop_name_field,
            ft.Row([email_field, phone_field]),
            adress_field,
            ft.Row([rccm_field, ifu_field]),
            ft.Row([owner_lastname_field, owner_firstname_field]),
            ft.Row([select_logo]),
            # ft.Row([ft.Container(logo_file_state["error"], margin=ft.margin.only(top=-16, left=15, bottom=-20))]),
            ft.Row([save_shop_info])
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
    ),
    padding=ft.padding.only(right=18)

    )

    return shop_register_container
