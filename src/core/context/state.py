import flet as ft
from utils.types import UserType
from .current_user import CurrentUser
from core.auth.BasePermission import Permission




class RstockState():


    ##################################################################
    ############################## STATE #############################
    ##################################################################
    #                                                                #
    #  Classe centralisant et gérant l’état global de l’application  #
    #      en mémoire, incluant les règles de modification et la     # 
    #         synchronisation avec la couche de persistance.         #
    #                                                                #
    ##################################################################
    ############################## CORE ##############################
    ##################################################################
    
    prefix = "rstate"

    
    def __init__(self, page):
        self.page = page
    
    def _get_key(self, key):
        return f"{self.prefix}_{key}"

    def _set(self, key, data):
        key = self._get_key(key)
        self.page.session.store.set(key, data)
    
    def _get(self, key):
        key = self._get_key(key)
        data = self.page.session.store.get(key)
        return data
    
    def _destroyer(self, key):
        key = self._get_key(key)
        self.page.session.store.remove(key)
    

    ##################################################################
    ############################# STATE ##############################
    ##################################################################
    
    
    ##### USER #####

    def set_user(self, user: UserType):
        self._set("user", user)

    def get_user(self) -> UserType | None :
        return self._get("user")

    def get_current_user(self) -> CurrentUser | None:
        return CurrentUser(self.get_user())

    def is_authenticated(self) -> bool:
        return self.get_user() is not None
    
    def clear_user(self):
        self._destroyer("user")


    def can(self, permission:Permission)->bool:
        user = self.get_current_user()
        return user.has_permission(permission)

