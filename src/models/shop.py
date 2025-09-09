from peewee import *
from models.akonta import AkontaObject


class Shop(AkontaObject):
    name = CharField(max_length=50)
    logo = CharField(max_length=500, null=True)
    email = CharField(max_length=50)
    phone = CharField(max_length=20)
    adress = CharField(max_length=150, null=True)
    balance = DecimalField(decimal_places=2, default=0)
    ifu = CharField(max_length=100, null=True)
    rccm = CharField(max_length=100, null=True)
    manager = CharField(max_length=150)

    def __str__(self):
        return self.name


