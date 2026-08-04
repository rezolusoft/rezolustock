from typing import TypedDict, NotRequired
from datetime import datetime
from core.auth.BasePermission import Permission



class ShopType(TypedDict):
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



class UserType(TypedDict):
    id: int
    avatar : NotRequired[str]
    first_name : str
    last_name : str
    email : str
    phone : str
    account_type : str
    last_seen : datetime | None
    shop : NotRequired[ShopType]
    permissions : set[Permission]
