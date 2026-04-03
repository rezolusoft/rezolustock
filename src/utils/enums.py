from enum import Enum

class BaseEnum(Enum):
    
    @classmethod
    def keys(cls):
        return [k.name for k in cls]
    
    @classmethod
    def values(cls):
        return [k.value for k in cls]
    
    @classmethod
    def items(cls):
        return [(k.name, k.value) for k in cls]
    


class TransactionTypeEnums(BaseEnum):
    INCOME = "income"
    EXPENSE = "expense"

class CurrencyTypeEnums(BaseEnum):
    XOF = "Franc CFA BCEAO"
    XAF = "Franc CFA CEMAC"
    USD = "Dollars US"
    EUR = "Euro"


class AccountTypeEnums(BaseEnum):
    OWNER = "owner"
    ADMIN = "admin"
    SELLER = "seller"

