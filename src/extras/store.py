class RStockStore():
    """
    Store
    Classe permettant de gerer le stockage de données utilisateur
    produite et exploitée par l'application

    liste des donnees: \n
    db_init -> permet de stocker l'etat de la bd

    """
    prefix = "rstock"

    def __init__(self, page):
        self.page = page
    
    def set(self, key, data):
        key = f"{self.prefix}_{key}"
        self.page.client_storage.set(key, data)

    def get(self, key):
        key = f"{self.prefix}_{key}"
        return self.page.client_storage.get(key)
    
    def check(self, key):
        key = f"{self.prefix}_{key}"
        return self.page.client_storage.contains_key(key)
    
    def destroy(self, key):
        key = f"{self.prefix}_{key}"
        self.page.client_storage.remove(key)
        return not self.page.client_storage.contains_key(key)