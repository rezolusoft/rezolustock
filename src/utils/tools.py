import uuid
import os
import shutil
import re



def id_generator()->uuid:

    """Genere un identifiant universel unique"""

    return uuid.uuid4()


def product_code_generator()->str:

    """Genere un code unique pour un objet produit"""

    rand_code = id_generator().hex[:5]
    return f"PROD-{rand_code.upper()}"


def category_code_generator()->str:

    """Genere un code unique pour un objet category"""
    rand_code = id_generator().hex[:5]
    return f"CAT-{rand_code.upper()}"


def sale_code_generator()->str:

    """Genere un code unique pour un objet vente"""
    rand_code = id_generator().hex[:5]
    return f"SALE-{rand_code.upper()}"

def invoice_code_generator()->str:

    """Genere un code unique pour un objet vente"""
    rand_code = id_generator().hex[:5]
    return f"INVOICE-{rand_code.upper()}"


def local_file_uploader(_file, _dir="img"):

    if not getattr(_file, "path", None):
        raise ValueError(
            f"Impossible d'obtenir le chemin local du fichier : {_file}"
        )

    media_dir = os.path.join(os.getcwd(), "media")
    os.makedirs(media_dir, exist_ok=True)

    base, ext = os.path.splitext(_file.name)
    filename = f"{base}_{id_generator().hex[:5]}{ext}"

    upload_dir = os.path.join(media_dir, _dir)
    os.makedirs(upload_dir, exist_ok=True)

    dest = os.path.join(upload_dir, filename)

    print("SOURCE :", _file.path)
    print("DEST   :", dest)

    shutil.copy2(_file.path, dest)

    return dest


#def local_file_uploader(_file, _dir="img"):
    media_dir = os.path.join(os.getcwd(), 'media')
    os.makedirs(media_dir, exist_ok=True)
    file = _file.path
    name = _file.name
    name = name.split(".")
    name = f"{name[0]}_{id_generator().hex[:5]}.{name[1]}"
    dest = os.path.join(media_dir, _dir)
    os.makedirs(dest, exist_ok=True)
    dest = os.path.join(dest, name)
    shutil.copy(file, dest)

    return dest
