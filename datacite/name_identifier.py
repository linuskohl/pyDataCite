from marshmallow import Schema, fields, ValidationError, pre_load, post_load


class NameIdentifier(object):
    '''NameIdentifier object'''

    def __init__(self, nameIdentifier, nameIdentifierScheme, schemeURI=None):
        self.nameIdentifier = nameIdentifier
        self.nameIdentifierScheme = nameIdentifierScheme
        self.schemeURI = schemeURI


class NameIdentifierSchema(Schema):
    '''NameIdentifier object schema'''

    nameIdentifier = fields.String(required=True)
    nameIdentifierScheme = fields.String(required=True)
    schemeURI = fields.String()

    @post_load
    def make_name_identifier(self, data):
        '''Return NameIdentifier object after loading'''
        return NameIdentifier(**data)
