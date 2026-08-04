from models.rezolustock import RstockObject
from utils.enums import AccountTypeEnums as account
from peewee import *


class User(RstockObject):
    """
        Represente un utilisateur du systeme
        Un utilisateur peut etre un admin ou un vendeur
    """
    avatar = CharField(max_length=500, null=True)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = CharField(max_length=100, null=False, unique=True, index=True)
    phone = CharField(max_length=50, null=False, unique=True, index=True)
    password = CharField(max_length=500)
    account_type = CharField(max_length=10, choices=account.items(), default=account.SELLER.value)
    last_seen = DateTimeField(null=True)


    def __str__(self):
        
        return f"{self.first_name} {self.last_name}"
    
    


    



