from marshmallow import fields, validate
from app.utils import (Sex, EmployeeIndex, IsPrimary, CustomerType, CustomerRelationType,
                       DecresedIndex, AddressType, ActivityIndex, CustomerSegmentation)

from app.extensions import ma


class PredictionRequestSchema(ma.Schema):
    customer_code = fields.String(
        required=True, validate=validate.Length(min=1))
    customer_name = fields.String()
    customer_age = fields.String()
    customer_employee_index = fields.Enum(EmployeeIndex, by_value=True)
    customer_gender = fields.Enum(Sex, by_value=True)
    customer_country = fields.String()
    customer_join_date = fields.Date()
    customer_is_new = fields.Boolean()
    customer_seniority = fields.String()
    customer_primary = fields.Enum(IsPrimary, by_value=True)
    customer_type = fields.Enum(CustomerType, by_value=True)
    customer_relation_type = fields.Enum(CustomerRelationType, by_value=True)
    customer_residence_index = fields.Boolean()
    customer_foreign_index = fields.Boolean()
    customer_spouse_index = fields.Boolean()
    customer_channel = fields.String()
    customer_decreased_index = fields.Enum(DecresedIndex, by_value=True)
    customer_address_type = fields.Enum(AddressType, by_value=True)
    customer_province_code = fields.String()
    customer_province_name = fields.String()
    customer_activity_index = fields.String()
    customer_gross_income = fields.Float()
    customer_segmentation = fields.Enum(CustomerSegmentation, by_value=True)
    date_created = fields.DateTime()

    class Meta:
        ordered = True
