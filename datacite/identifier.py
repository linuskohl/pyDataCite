from marshmallow import Schema, fields, ValidationError, pre_load, post_load


class Identifier(object):
    '''Identifier object'''

    def __init__(self, identifier, identifierType):
        self.identifier = identifier
        self.identifierType = identifierType


class IdentifierSchema(Schema):
    '''Identifier object schema'''

    identifier = fields.String(required=True)
    identifierType = fields.String(required=True)

    @post_load
    def make_identifier(self, data):
        '''Return Identifier object after loading'''
        return Identifier(**data)
