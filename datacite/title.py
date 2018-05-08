from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from marshmallow_enum import EnumField
from .enums.enums import TitleTypeEnum

# A name or title by which a resource is known

class Title(object):
    def __init__(self, title, lang=None, type=None, titleType=None):
        self.title = title
        self.type = type
        self.titleType = titleType
        self.lang = lang

class TitleSchema(Schema):
    title = fields.String(required=True)
    # WARNING: This field has been superseded by 'titleType'
    type = fields.String()
    # TitleTypeEnum
    titleType = EnumField(TitleTypeEnum)
    lang = fields.String()

    @post_load
    def make_title(self, data):
        return Title(**data)