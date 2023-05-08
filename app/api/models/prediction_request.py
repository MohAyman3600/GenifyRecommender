from datetime import datetime

from app.extensions import mongo
from app.utils import (
    Sex, EmployeeIndex, IsPrimary, CustomerType,
    CustomerRelationType, DecresedIndex, AddressType,
    CustomerSegmentation
)


class PredictionRequest(mongo.Document):
    customer_code = mongo.StringField(required=True, unique=True)
    customer_name = mongo.StringField()
    customer_age = mongo.StringField()
    customer_employee_index = mongo.EnumField(EmployeeIndex)
    customer_gender = mongo.EnumField(Sex)
    customer_country = mongo.StringField()
    customer_join_date = mongo.DateField()
    customer_is_new = mongo.BooleanField()
    customer_seniority = mongo.StringField()
    customer_primary = mongo.EnumField(IsPrimary)
    customer_type = mongo.EnumField(CustomerType)
    customer_relation_type = mongo.EnumField(CustomerRelationType)
    customer_residence_index = mongo.BooleanField()
    customer_foreign_index = mongo.BooleanField()
    customer_spouse_index = mongo.BooleanField()
    customer_channel = mongo.StringField()
    customer_decreased_index = mongo.EnumField(DecresedIndex)
    customer_address_type = mongo.EnumField(AddressType)
    customer_province_code = mongo.StringField()
    customer_province_name = mongo.StringField()
    customer_activity_index = mongo.StringField()
    customer_gross_income = mongo.FloatField()
    customer_segmentation = mongo.EnumField(CustomerSegmentation)

    date_created = mongo.DateTimeField(default=datetime.utcnow)
