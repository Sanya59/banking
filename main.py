from decimal import Decimal
from model_db import *

with db:
    db.create_tables([Clients,Card,Operation,Telegram])