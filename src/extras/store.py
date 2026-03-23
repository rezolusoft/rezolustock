import flet as ft


class RStockStore():
    """
    Store
    Classe permettant de gerer le stockage de données utilisateur
    produite et exploitée par l'application

    liste des donnees: \n
    db_init -> permet de stocker l'etat de la bd

    """
    prefix = "rstock"

    
    async def set(self, key, data):
        key = f"{self.prefix}_{key}"
        set = await ft.SharedPreferences().set(key, data)
        return set

    async def get(self, key):
        key = f"{self.prefix}_{key}"
        get = await ft.SharedPreferences().get(key)
        return get
    
    async def check(self, key):
        key = f"{self.prefix}_{key}"
        check = await ft.SharedPreferences().contains_key(key)
        return check
    
    async def destroy(self, key):
        key = f"{self.prefix}_{key}"
        await ft.SharedPreferences().remove(key)
        