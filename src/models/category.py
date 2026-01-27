from models.rezolustock import RstockObject
from extras.tools import category_code_generator
from peewee import *

class Category(RstockObject):
    """
        Represente la categorie d'un produit
    """
    code = CharField(default=category_code_generator, unique=True, index=True)
    name = CharField(max_length=150)
    description = TextField(null=True)
    image = CharField(max_length=500, null=True)
    parent = ForeignKeyField("self", null=True, backref="subcategories")


    def __str__(self):
        return f"{self.code} -> {self.name}"
