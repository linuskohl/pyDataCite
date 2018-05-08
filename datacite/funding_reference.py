from marshmallow import Schema, fields, ValidationError, pre_load, post_load


class FundingReference(object):
    '''FundingReference object'''

    def __init__(self, funderName=None, funderIdentifier=None, funderIdentifierType=None, awardTitle=None,
                 awardNumber=None):
        self.funderName = funderName
        self.funderIdentifier = funderIdentifier
        self.funderIdentifierType = funderIdentifierType
        self.awardTitle = awardTitle
        self.awardNumber = awardNumber


class FundingReferenceSchema(Schema):
    '''FundingReference object schema'''
    # Name of the funding provider
    funderName = fields.String()
    # Uniquely identifies a funding entity, according to various types.
    funderIdentifier = fields.Nested('FunderIdentifierSchema', many=False)
    funderIdentifierType = fields.String()
    awardTitle = fields.String()
    awardNumber = fields.Nested('AwardNumberSchema', many=False)

    @post_load
    def make_funding_reference(self, data):
        '''Return FundingReference object after loading'''
        return FundingReference(**data)
