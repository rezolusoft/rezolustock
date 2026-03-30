from typing import TypedDict, NotRequired

class Shop(TypedDict):
    id: int
    name : str
    email: str
    phone: str
    adress: str
    ifu: str
    balance: str 
    rccm: str
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    manager : NotRequired[str]
    logo: str

class User(TypedDict):
    id: int
    avatar : NotRequired[str]
    first_name : str
    last_name : str
    email : str
    phone : str
    account_type : str
    shop : Shop
    last_seen : str
