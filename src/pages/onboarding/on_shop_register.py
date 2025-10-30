import flet as ft
from extras.tools import is_valid_email
from pathlib import Path




def on_shop_register(page) -> ft.Control:

    # CHAMPS DU FORMULAIRE D'ENREGISTREMENT D'UNE BOUTIQUE

    shop_name_field = ft.TextField(hint_text="*Nom de votre boutique", border_radius=10)

    email_field = ft.TextField(hint_text="*Adresse Email", border_radius=10, expand=1)

    phone_field = ft.TextField(hint_text="*Numéro de téléphone", border_radius=10, expand=1)

    adress_field = ft.TextField(hint_text="*Adresse de la boutique", border_radius=10)

    rccm_field = ft.TextField(hint_text="Registre de commerce", border_radius=10, expand=1)

    ifu_field = ft.TextField(hint_text="Numéro IFU", border_radius=10, expand=1)

    owner_firstname_field = ft.TextField(hint_text="*Prénoms du Propriétaire",border_radius=10, expand=1)

    owner_lastname_field = ft.TextField(hint_text="*Nom du Propriétaire",border_radius=10, expand=1)

    # CHAMPS DU FORMULAIRE D'ENREGISTREMENT D'UNE BOUTIQUE
    

    # FONCTION DE GESTION D'AJOUT DE FICHIER
    

    logo_file_state = {
        "file" : None,
        "error" : ft.Text("", color=ft.Colors.ERROR, size=12 )
    }

    def on_logo_selected(e: ft.FilePickerResultEvent):
        if e.files:
            select_logo.text = f"logo sélectionné : {e.files[0].name}"
            logo_file_state["file"] = e.files[0]
            page.update()
            
        else:
            select_logo.text = "Ajouter votre logo / Aucun fichier sélectionné"
            page.update()
        

    # SELECTEUR DE FICHIER
    select_logo_dialog = ft.FilePicker(on_result=on_logo_selected)
    
    
    # BOUTON DECLENCHEUR DU SELECTEUR DE FICHIER
    select_logo = ft.ElevatedButton(
        "Ajouter votre logo / Aucun fichier sélectionné",
        icon=ft.Icons.UPLOAD_FILE_ROUNDED,
        expand=1,
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(vertical=20),
            shape=ft.RoundedRectangleBorder(10)
        ),

        on_click=lambda _: select_logo_dialog.pick_files(allow_multiple=False, initial_directory=Path.home()/"Pictures", file_type=ft.FilePickerFileType.IMAGE)
      )
    
    # AJOUT DU SELECTEUR DE FICHIER A LA PAGE
    page.overlay.append(select_logo_dialog)
    page.update()


    # FONCTION DE TRAITEMENT DE FORMULAIRE
    def form_handler(e):

        # RECUPERATION DES DONNEES ENTRER PAR L'UTILISATEUR
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
        if not shop["name"].value.strip():
            shop["name"].error_text = "Veuillez renseigner le nom de votre boutique/commerce"
        else:
            shop["name"].error_text = None

        # Validation de l'email de boutique
        if not shop["email"].value.strip():
            shop["email"].error_text = "Veuillez renseigner une adresse email valide"
        else:
            shop["email"].error_text = None

        if is_valid_email(shop["email"].value.strip()):
            shop["email"].error_text = None
        else:
            shop["email"].error_text = "Veuillez renseigner une adresse email valide"
        
        # Validation du numéro de téléphone de boutique
        if not shop["phone"].value.strip():
            shop["phone"].error_text = "Veuillez renseigner un numéro de téléphone"
        else:
            shop["phone"].error_text = None
        
        # Validation du l'adresse de la boutique
        if not shop["adress"].value.strip():
            shop["adress"].error_text = "Veuillez renseigner l'adresse de la boutique"
        else:
            shop["adress"].error_text = None
        
        # Validation du prénom du gérant de la boutique
        if not shop["first_name"].value.strip():
            shop["first_name"].error_text = "Veuillez renseigner votre Prénom"
        else:
            shop["first_name"].error_text = None
        
        # Validation du nom du gérant de la boutique
        if not shop["last_name"].value.strip():
            shop["last_name"].error_text = "Veuillez renseigner votre Nom"
        else:
            shop["last_name"].error_text = None

        if not logo_file_state["file"]:
            logo_file_state["error"].value = "Vous devez ajouter un logo"
        else:
            logo_file_state["error"].value = None
        
        

        page.update()
    
    save_shop_info = ft.ElevatedButton(
        "Sauvegarder",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(10),
            padding=15,
            bgcolor=ft.Colors.SECONDARY,
            text_style=ft.TextStyle(
                font_family="PoppinsSemiBold",
                size=20
            )
        ),
        color=ft.Colors.ON_SURFACE, 
        expand=1,
        on_click=form_handler
        )

    shop_register_container = ft.Container(ft.Column(
        expand=True,
        controls=[
            ft.Text("Enregistrer votre boutique", size=25, font_family="PoppinsBold", color=ft.Colors.ON_SURFACE),
            shop_name_field,
            ft.Row([email_field, phone_field]),
            adress_field,
            ft.Row([rccm_field, ifu_field]),
            ft.Row([owner_lastname_field, owner_firstname_field]),
            ft.Row([select_logo]),
            ft.Row([ft.Container(logo_file_state["error"], margin=ft.margin.only(top=-20, left=15, bottom=5))]),
            ft.Row([save_shop_info])
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    ),
    padding=ft.padding.only(right=20)

    )

    return shop_register_container
