from marshmallow import Schema, fields, ValidationError, pre_load, post_load

class Right(object):
    def __init__(self, rights=None, rightsURI=None, lang=None):
        self.rights = rights
        self.rightsURI = rightsURI
        self.lang = lang


class RightSchema(Schema):
    rights = fields.String()
    rightsURI = fields.Url()
    lang = fields.String()

    @post_load
    def make_right(self, data):
        return Right(**data)
