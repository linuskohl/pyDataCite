from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from .alternate_identifier import AlternateIdentifierSchema
from .award_number import AwardNumberSchema
from .contributor import ContributorSchema
from .creator import CreatorSchema
from .description import DescriptionSchema
from .funder_identifier import FunderIdentifierSchema
from .funding_reference import FundingReferenceSchema
from .geo_location import GeoLocationSchema
from .identifier import IdentifierSchema
from .name_identifier import NameIdentifierSchema
from .resource_type import ResourceTypeSchema
from .right import RightSchema
from .subject import SubjectSchema
from .title import TitleSchema
from .date import DateSchema
from .related_identifier import RelatedIdentifierSchema


class Entry(object):
    def __init__(self, identifier, creators, titles, publisher, publicationYear, resourceType, contributors=None,
                 dates=None, language=None, alternateIdentifiers=None, relatedIdentifiers=None, size=None, formats=None,
                 version=None, rightsList=None, descriptions=None, fundingReferences=None, geoLocations=None,
                 subjects=None):
        self.identifier = identifier
        self.creators = creators
        self.titles = titles
        self.publisher = publisher
        self.publicationYear = publicationYear
        self.resourceType = resourceType
        self.contributors = contributors
        self.dates = dates
        self.language = language
        self.alternateIdentifiers = alternateIdentifiers
        self.relatedIdentifiers = relatedIdentifiers
        self.size = size
        self.formats = formats
        self.version = version
        self.rightsList = rightsList
        self.descriptions = descriptions
        self.fundingReferences = fundingReferences
        self.geoLocations = geoLocations
        self.subjects = subjects


class EntrySchema(Schema):
    identifier = fields.Nested('IdentifierSchema', many=False, required=True)
    creators = fields.Nested('CreatorSchema', many=True, required=True)
    titles = fields.Nested('TitleSchema', many=True, required=True)
    # The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. This property will be used to formulate the citation, so consider the prominence of the role. In the case of datasets, \"publish\" is understood to mean making the data available to the community of researchers.
    publisher = fields.String(required=True)
    # Year when the data is made publicly available. If an embargo period has been in effect, use the date when the embargo period ends. In the case of datasets, \"publish\" is understood to mean making the data available on a specific date to the community of researchers. If there is no standard publication year value, use the date that would be preferred from a citation perspective.
    publicationYear = fields.Integer(required=True)
    subjects = fields.Nested('SubjectSchema', many=True)
    contributors = fields.Nested('ContributorSchema', many=True)
    dates = fields.Nested('DateSchema', many=True)
    language = fields.String()
    resourceType = fields.Nested('ResourceTypeSchema', many=False, required=True)
    alternateIdentifiers = fields.Nested('AlternateIdentifierSchema', many=True)
    relatedIdentifiers = fields.Nested('RelatedIdentifierSchema', many=True)
    # Unstructured size information about the resource
    size = fields.List(fields.String())

    # Technical format of the resource. Use file extension or MIME type where possible.
    formats = fields.List(fields.String())

    # Version number of the resource. If the primary resource has changed the version number increases.
    # Register a new identifier for a major version change. Individual stewards need to determine which are
    # major vs. minor versions. May be used in conjunction with properties 11 and 12 (AlternateIdentifier and
    # RelatedIdentifier) to indicate various information updates. May be used in conjunction with property 17
    # (Description) to indicate the nature and file/record range of version.
    version = fields.String()

    # Any rights information for this resource.Provide a rights management statement for the resource or reference a
    # service providing such information.Include embargo information if applicable.Use the complete title of a
    # license and include version information if applicable."
    rightsList = fields.Nested('RightSchema', many=True)

    # All additional information that does not fit in any of the other categories. May be used for technical information.
    # It is a best practice to supply a description.
    descriptions = fields.Nested('DescriptionSchema', many=True)

    # Information about financial support (funding) for the resource being registered.
    fundingReferences = fields.Nested('FundingReferenceSchema', many=True)

    # Spatial region or named place where the data was gathered or about which the data is focused.
    #geoLocations = fields.Nested('GeoLocationSchema', many=True)

    @post_load
    def make_entry(self, data):
       return Entry(**data)
