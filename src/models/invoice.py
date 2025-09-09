from models.akonta import AkontaObject
from models.customer import AkontaCustomer
from models.sale import AkontaSale
from extras.tools import invoice_code_generator
from peewee import *


class Invoice(AkontaObject):
    """
        Represente le recu d'une operation de vente
    """
    code = CharField(default=invoice_code_generator)
    sale = ForeignKeyField(AkontaSale)
    customer = ForeignKeyField(AkontaCustomer, backref="invoices")
    comment = TextField(null=True)

    
    def __str__(self):
        return f"{self.code} - {self.created_at}"

