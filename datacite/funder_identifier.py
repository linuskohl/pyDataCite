from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from marshmallow_enum import EnumField
from .enums.enums import FunderIdentifierTypeEnum

# Uniquely identifies a funding entity, according to various types

class FunderIdentifier(object):
    def __init__(self, funderIdentifier, funderIdentifierType):
        self.funderIdentifier = funderIdentifier
        self.funderIdentifierType = funderIdentifierType

class FunderIdentifierSchema(Schema):

    funderIdentifier = fields.String(required=True)

    # FunderIdentifierType
    funderIdentifierType = EnumField(FunderIdentifierTypeEnum, required=True, by_value=True)

    @post_load
    def make_funder_identifier(self, data):
        return FunderIdentifier(**data)