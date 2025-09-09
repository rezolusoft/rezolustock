from models.akonta import AkontaObject
from extras.tools import id_generator
from models.user import AkontaUser
from extras.enums import TransactionTypeEnums
from peewee import *

class Transaction(AkontaObject):
    title = CharField()
    transaction_id = UUIDField(default=id_generator)
    amount = DecimalField()
    type = CharField(choices=TransactionTypeEnums.items())
    description = TextField(null=True)
    issuer = ForeignKeyField(AkontaUser, backref="transactions")

    def __str__(self):
        return f"{self.title} -> {self.amount}"
