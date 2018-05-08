from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from marshmallow_enum import EnumField
from .enums.enums import NameTypeEnum


# The main researchers involved working on the data, or the authors of the publication in
# priority order. May be a corporate/institutional or personal name

class Creator(object):
    '''Creator object'''

    def __init__(self, creatorName, nameType=None, givenName=None, familyName=None, nameIdentifiers=None,
                 affiliations=None):
        # Format: Family, Given
        self.creatorName = creatorName
        self.nameType = nameType
        self.givenName = givenName
        self.familyName = familyName
        self.nameIdentifiers = nameIdentifiers
        self.affiliations = affiliations


class CreatorSchema(Schema):
    '''Creator object schema'''
    creatorName = fields.String(required=True)
    # NameTypeEnum
    nameType = EnumField(NameTypeEnum)
    givenName = fields.String()
    familyName = fields.String()
    nameIdentifiers = fields.Nested('NameIdentifierSchema', many=True)
    affiliations = fields.List(fields.String())

    @post_load
    def make_creator(self, data):
        '''Return Creator object after loading'''
        return Creator(**data)
