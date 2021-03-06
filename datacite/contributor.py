from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from marshmallow_enum import EnumField
from .enums.enums import NameTypeEnum, ContributorTypeEnum


# The institution or person responsible for collecting, creating, or otherwise contributing to
# the developement of the dataset

class Contributor(object):
    '''Contributor object'''

    def __init__(self, contributorName, nameType=None, contributorType=None, nameIdentifiers=None, affiliations=None):
        # The personal name format should be: Family, Given
        self.contributorName = contributorName
        self.nameType = nameType
        self.contributorType = contributorType
        self.nameIdentifiers = nameIdentifiers
        self.affiliations = affiliations


class ContributorSchema(Schema):
    '''Contributor object schema'''

    contributorName = fields.String(required=True)
    # NameTypeEnum
    nameType = EnumField(NameTypeEnum)
    # ContributorTypeEnum
    contributorType = EnumField(ContributorTypeEnum)
    nameIdentifiers = fields.Nested('NameIdentifierSchema', many=True)
    affiliations = fields.List(fields.String())

    @post_load
    def make_contributor(self, data):
        '''Return Contributor object after loading'''
        return Contributor(**data)
