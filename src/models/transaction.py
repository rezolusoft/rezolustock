from models.rezolustock import RstockObject
from utils.tools import id_generator
from models.user import User
from utils.enums import TransactionTypeEnums
from peewee import *

class Transaction(RstockObject):
    title = CharField()
    transaction_id = UUIDField(default=id_generator)
    amount = DecimalField(decimal_places=2)
    type = CharField(choices=TransactionTypeEnums.items())
    description = TextField(null=True)
    issuer = ForeignKeyField(User, backref="transactions")

    def __str__(self):
        return f"{self.title} -> {self.amount}"
