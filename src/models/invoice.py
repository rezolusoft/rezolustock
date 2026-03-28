from models.rezolustock import RstockObject
from models.customer import Customer
from models.sale import Sale
from extras.tools import invoice_code_generator
from peewee import *


class Invoice(RstockObject):
    """
        Represente le recu d'une operation de vente
    """
    code = CharField(default=invoice_code_generator)
    sale = ForeignKeyField(Sale)
    customer = ForeignKeyField(Customer, backref="invoices")
    comment = TextField(null=True)

    
    def __str__(self):
        return f"{self.code} - {self.created_at}"

