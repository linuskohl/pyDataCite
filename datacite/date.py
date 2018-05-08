from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from marshmallow_enum import EnumField
from .enums.enums import DateTypeEnum


# Different dates relevant to the work

class Date(object):
    '''Date object'''

    def __init__(self, dateType, date=None, dateInformation=None):
        self.date = date
        self.dateType = dateType
        self.dateInformation = dateInformation


class DateSchema(Schema):
    '''Date object schema'''

    # YYYY,YYYY-MM-DD, YYYY-MM-DDThh:mm:ssTZD or any other format or level of granularity described in W3CDTF.
    # Use RKMS-ISO8601 standard for depicting date ranges.
    date = fields.Date()
    # DateTypeEnum
    dateType = EnumField(DateTypeEnum, required=True)
    # Specific information about the date
    dateInformation = fields.String()

    @post_load
    def make_date(self, data):
        '''Return Date object after loading'''
        return Date(**data)
