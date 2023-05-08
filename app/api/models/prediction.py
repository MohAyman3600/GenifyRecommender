from datetime import datetime


from app.extensions import mongo


class Prediction(mongo.Document):
    customer_code = mongo.StringField(required=True, uniqu=True)
    saving_account = mongo.BooleanField()
    guarantees = mongo.BooleanField()
    current_accounts = mongo.BooleanField()
    derivada_account = mongo.BooleanField()
    payroll_account = mongo.BooleanField()
    junior_account = mongo.BooleanField()
    mas_particular_account = mongo.BooleanField()
    particular_account = mongo.BooleanField()
    particular_plus_account = mongo.BooleanField()
    short_term_deposits = mongo.BooleanField()
    medium_term_deposits = mongo.BooleanField()
    long_term_deposits = mongo.BooleanField()
    e_account = mongo.BooleanField()
    funds = mongo.BooleanField()
    mortgage = mongo.BooleanField()
    pensions = mongo.BooleanField()
    loans = mongo.BooleanField()
    taxes = mongo.BooleanField()
    credit_card = mongo.BooleanField()
    securities = mongo.BooleanField()
    home_account = mongo.BooleanField()
    payroll = mongo.BooleanField()
    pensions_2 = mongo.BooleanField()
    direct_debit = mongo.BooleanField()

    date_created = mongo.DateTimeField(default=datetime.utcnow)
