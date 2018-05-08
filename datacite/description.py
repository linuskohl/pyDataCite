from marshmallow import Schema, fields, ValidationError, pre_load, post_load


class Description(object):
    '''Description object'''
    def __init__(self, description, descriptionType, lang=None):
        self.description = description
        self.descriptionType = descriptionType
        self.lang = lang


class DescriptionSchema(Schema):
    '''Description object schema'''
    description = fields.String(required=True)
    # The type of the description
    descriptionType = fields.String(required=True)
    lang = fields.String()

    @post_load
    def make_description(self, data):
        '''Return Description object after loading'''
        return Description(**data)
