from marshmallow import Schema, fields, ValidationError, pre_load, post_load


# An identifier or identifiers other than the primary Identifier applied to the resource being
# registered. This may be any alphanumeric string which is unique within its domain of issue.
# May be used for local identifiers. AlternateIdentifier should be used for another
# identifier of the same instance (same location, same file).
class AlternateIdentifier(object):
    '''AlternateIdentifier object'''

    def __init__(self, alternateIdentifier, alternateIdentifierType):
        self.alternateIdentifier = alternateIdentifier
        self.alternateIdentifierType = alternateIdentifierType


class AlternateIdentifierSchema(Schema):
    '''AlternateIdentifier object schema'''

    alternateIdentifier = fields.String(required=True)
    alternateIdentifierType = fields.String(required=True)

    @post_load
    def make_alternate_identifier(self, data):
        '''Return AlternateIdentifier object after loading'''
        return AlternateIdentifier(**data)
