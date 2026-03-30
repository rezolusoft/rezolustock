from models.rezolustock import RstockObject
from models.category import Category
from extras.tools import product_code_generator
from peewee import *


class Product(RstockObject):
    """
        Represente un produit
    """
    name = CharField(max_length=150)
    description = TextField(null=True)
    category = ForeignKeyField(Category, backref="products")
    code = CharField(default=product_code_generator, unique=True, index=True)
    image = CharField(max_length=500, null=True)
    price = DecimalField(decimal_places=2, null=True)
    cost = DecimalField(decimal_places=2, null=True)

    quantity = IntegerField(default=5)
    quantity_alert = IntegerField(default=3)

    unit = CharField(null=True)
    
    def __str__(self):
        return f"{self.code} -> {self.name}"
