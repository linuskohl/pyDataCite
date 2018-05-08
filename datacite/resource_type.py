from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from marshmallow_enum import EnumField
from .enums.enums import ResourceTypeEnum


# The type of a resource. You may enter an additional free text description. The format is open,
# but the preferred format is a single term of some detail so that a pair can be formed with the sub-property
class ResourceType(object):
    '''ResourceType object'''

    def __init__(self, resourceTypeGeneral, resourceType=None):
        self.resourceTypeGeneral = resourceTypeGeneral
        self.resourceType = resourceType


class ResourceTypeSchema(Schema):
    '''ResourceType object schema'''

    resourceTypeGeneral = EnumField(ResourceTypeEnum, required=True)
    resourceType = fields.String()

    @post_load
    def make_resource_type(self, data):
        '''Return ResourceType object after loading'''
        return ResourceType(**data)
