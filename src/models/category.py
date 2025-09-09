from models.akonta import AkontaObject
from extras.tools import category_code_generator
from peewee import *

class Category(AkontaObject):
    """
        Represente la categorie d'un produit
    """
    code = CharField(default=category_code_generator, unique=True, index=True)
    name = CharField(max_length=150)
    description = TextField(null=True)
    parent = ForeignKeyField("self", null=True, backref="subcategories")


    def __str__(self):
        return f"{self.code} -> {self.name}"
