from datetime import datetime, date, time
from decimal import Decimal
import uuid


def rstore_serializer(obj):
    # Write a strong serializer to serialize store data
    if isinstance(obj, datetime):
        return obj.isoformat()
    
    if isinstance(obj, date):
        return obj.isoformat()
    
    if isinstance(obj, time):
        return obj.isoformat()
    
    if isinstance(obj, Decimal):
        return str(obj)

    if isinstance(obj, uuid.UUID):
        return str(obj)
    
    if isinstance(obj, bytes):
        return obj.decode("utf-8")
    
    
    raise TypeError(f"Type {type(obj)} not serializable")