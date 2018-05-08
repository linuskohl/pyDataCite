from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from marshmallow_enum import EnumField
from .enums.enums import RelatedIdentifierTypeEnum, ResourceTypeEnum, RelatedIdentifierRelationTypeEnum


# Identifiers of related resources. Use this property to indicate subsets of properties, as appropriate
class RelatedIdentifier(object):
    def __init__(self, relatedIdentifier, relatedIdentifierType, relationType, resourceTypeGeneral=None,
                 relatedMetadataScheme=None, schemeURI=None):
        self.relatedIdentifier = relatedIdentifier
        self.relatedIdentifierType = relatedIdentifierType
        self.relationType = relationType
        self.resourceTypeGeneral = resourceTypeGeneral
        self.relatedMetadataScheme = relatedMetadataScheme
        self.schemeURI = schemeURI


class RelatedIdentifierSchema(Schema):
    relatedIdentifier = fields.String(required=True)

    # RelatedIdentifierTypeEnum
    relatedIdentifierType = EnumField(RelatedIdentifierTypeEnum, required=True)

    #  RelatedIdentifierRelationTypeEnum
    relationType = EnumField(RelatedIdentifierRelationTypeEnum, required=True)

    # RelatedIdentifierResourceTypeEnum
    resourceTypeGeneral = EnumField(ResourceTypeEnum)

    relatedMetadataScheme = fields.String()

    schemeURI = fields.String()

    @post_load
    def make_related_identifier(self, data):
        return RelatedIdentifier(**data)
