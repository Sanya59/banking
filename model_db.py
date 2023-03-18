from peewee import *
import os

db = SqliteDatabase(os.path.abspath('bank.db'))


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Clients(BaseModel):
    Surname = CharField()
    Name = CharField()
    Middle_name = CharField()
    series_and_number = FloatField()
    city_registration = CharField()
    birthday = DateField()
    gender = CharField()
    phone_number = IntegerField()
    codeword = CharField()
    valid = CharField()

    class Meta:
        db_table = 'clients'


class Card(BaseModel):
    Surname = CharField()
    Name = CharField()
    Middle_name = CharField()
    series_and_number_passport = FloatField()
    date_of_creation = DateField()
    city_registration = CharField()
    card_tariff = CharField()
    card_number = IntegerField()
    card_uid = IntegerField()
    card_expiry_date = DateField()
    card_cvc = IntegerField()
    card_sum = FloatField()
    valid = CharField()

    class Meta:
        db_table = 'cards'


class Operation(BaseModel):
    id_card = IntegerField()
    operation_type = CharField()
    date_of_creation_operation = DateTimeField()
    city_of_operation = CharField()
    card_tariff = CharField()
    card_number = IntegerField()
    short_message = CharField()
    payees_card_number = IntegerField(null=True)
    sum_operation = FloatField()
    status = CharField()
    message = CharField()

    class Meta:
        # database = db
        db_table = 'operations'


class Telegram(BaseModel):
    series_and_number_passport = IntegerField()
    telegram_chat_id = CharField()

    class Meta:
        # database = db
        db_table = 'notifications'
