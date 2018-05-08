from marshmallow import Schema, fields, ValidationError, pre_load, post_load


# The code assigned by the funder to a sponsored award (grant)
class AwardNumber(object):
    '''AwardNumber object'''

    def __init__(self, awardNumber, awardURI=None):
        self.awardNumber = awardNumber
        self.awardURI = awardURI


class AwardNumberSchema(Schema):
    '''AwardNumber object schema'''

    awardNumber = fields.String(required=True)
    awardURI = fields.Url()

    @post_load
    def make_award_number(self, data):
        '''Return AwardNumber object after loading'''
        return AwardNumber(**data)
