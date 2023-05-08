from enum import Enum


class Sex(Enum):
    male = 'male'
    female = 'female'


class EmployeeIndex(Enum):
    active = 'active'
    ex_employed = 'ex-employed'
    filial = 'filial'
    not_employee = 'not-employee'
    pasive = 'pasive'


class IsPrimary(Enum):
    primary = 'primary'
    primary_im_month = "primary-in-month"


class CustomerType(Enum):
    primary = 'primary'
    co_owner = 'co-owner'
    potential = 'potential'
    former_primary = 'former-primary'
    former_co_owner = 'former-co-owner'


class CustomerRelationType(Enum):
    active = 'active'
    inactive = 'inactive'
    foremer_cutomer = 'former-customer'
    potential = 'potential'


class ActivityIndex(Enum):
    active_customer = 1
    inactive_customer = 0


class CustomerSegmentation(Enum):
    vip = 'vip'
    indviduals = 'indviduals'
    college_graduate = 'college-graduate'


class DecresedIndex(Enum):
    n = 'N'
    s = 'S'

class AddressType(Enum):
    primary = 'primary'
    none_primary = 'none-primary'
