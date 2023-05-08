from marshmallow import fields

from app.extensions import ma

class PredictionSchema(ma.Schema):
    customer_code = fields.String(required=True)
    saving_account = fields.Boolean()
    guarantees = fields.Boolean()
    current_accounts = fields.Boolean()
    derivada_account = fields.Boolean()
    payroll_account = fields.Boolean()
    junior_account = fields.Boolean()
    mas_particular_account = fields.Boolean()
    particular_account = fields.Boolean()
    particular_plus_account = fields.Boolean()
    short_term_deposits = fields.Boolean()
    medium_term_deposits = fields.Boolean()
    long_term_deposits = fields.Boolean()
    e_account = fields.Boolean()
    funds = fields.Boolean()
    mortgage = fields.Boolean()
    pensions = fields.Boolean()
    loans = fields.Boolean()
    taxes = fields.Boolean()
    credit_card = fields.Boolean()
    securities = fields.Boolean()
    home_account = fields.Boolean()
    payroll = fields.Boolean()
    pensions_2 = fields.Boolean()
    direct_debit = fields.Boolean()
    date_created = fields.DateTime()

    class Meta:
        ordered = True