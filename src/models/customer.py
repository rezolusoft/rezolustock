from models.rezolustock import RstockObject
from peewee import *


class Customer(RstockObject):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    company_name = CharField(max_length=100, null=True)
    email = CharField(max_length=50, null=True)
    phone = CharField(max_length=20)
    ifu = CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
