from models.rezolustock import RstockObject
from models.product import Product
from utils.tools import sale_code_generator, id_generator
from models.user import User
from peewee import *


class Sale(RstockObject):
    amount = DecimalField(decimal_places=2)
    sale_id = UUIDField(default=id_generator)
    code = CharField(default=sale_code_generator)
    seller = ForeignKeyField(User, backref="sales")

    def __str__(self):
        return self.code



class SaleItem(RstockObject):
    sale = ForeignKeyField(Sale, backref='items')
    product = ForeignKeyField(Product)
    quantity = IntegerField(default=1)
    price = DecimalField(decimal_places=2)
    comment = TextField(null=True)

    def __str__(self):
        return f"{self.sale.code} -> {self.product.name} x {self.quantity}"
