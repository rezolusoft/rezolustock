from utils.types import UserType
from core.auth.authorization import AuthorizationService
from core.auth.BasePermission import Permission
from utils.enums import AccountTypeEnums as account


class CurrentUser():

    """
        Représente un utilisateur dans l'etat courant de l'application
    """

    def __init__(self, data: UserType):
        self._data = data
        self._permissions = AuthorizationService.permissions(self.account_type)


    @property
    def id(self):
        return self._data["id"]

    @property
    def avatar(self):
        return self._data.get("avatar")


    @property
    def first_name(self):
        return self._data["first_name"]

    
    @property
    def last_name(self):
        return self._data["last_name"]

    
    @property
    def email(self):
        return self._data["email"]

    
    @property
    def phone(self):
        return self._data["phone"]

    
    @property
    def account_type(self):
        return self._data["account_type"]

    @property
    def last_seen(self):
        return self._data["last_seen"]

    @property
    def shop(self):
        return self._data["shop"]


    @property
    def shop_name(self):
        return self._data["shop"]["name"]


    @property
    def permissions(self):
        return self._permissions


    @property
    def initials(self):
        return f'{self.first_name[0]}{self.last_name[0]}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'



    def is_admin(self):
        return (self.account_type == account.ADMIN.value)
    

    def has_permission(self, permission:Permission):
        return permission in self.permissions

