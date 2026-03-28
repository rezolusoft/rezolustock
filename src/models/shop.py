from peewee import *
from models.rezolustock import RstockObject


class Shop(RstockObject):
    name = CharField(max_length=50)
    logo = CharField(max_length=500, null=True)
    email = CharField(max_length=100, null=False, unique=True, index=True)
    phone = CharField(max_length=20, null=False, unique=True, index=True)
    adress = CharField(max_length=150, null=True)
    balance = DecimalField(decimal_places=2, default=0)
    ifu = CharField(max_length=100, null=True)
    rccm = CharField(max_length=100, null=True)
    manager = CharField(max_length=150)

    def __str__(self):
        return self.name


