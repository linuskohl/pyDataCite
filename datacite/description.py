from marshmallow import Schema, fields, ValidationError, pre_load, post_load


class Description(object):
    def __init__(self, description, descriptionType, lang=None):
        self.description = description
        self.descriptionType = descriptionType
        self.lang = lang


class DescriptionSchema(Schema):
    description = fields.String(required=True)

    # The type of the description
    descriptionType = fields.String(required=True)

    lang = fields.String()

    @post_load
    def make_description(self, data):
        return Description(**data)
