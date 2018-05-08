from enum import Enum


class TitleTypeEnum(Enum):
    AlternativeTitle = 'AlternativeTitle'
    Subtitle = 'Subtitle'
    TranslatedTitle = 'TranslatedTitle'
    Other = 'Other'


class DateTypeEnum(Enum):
    Accepted = 'Accepted'
    Available = 'Available'
    Collected = 'Collected'
    Copyrighted = 'Copyrighted'
    Created = 'Created'
    Issued = 'Issued'
    Submitted = 'Submitted'
    Updated = 'Updated'
    Valid = 'Valid'
    Other = 'Other'


class NameTypeEnum(Enum):
    Organisational = 'Organisational'
    Personal = 'Personal'


class ContributorTypeEnum(Enum):
    ContactPerson = 'ContactPerson'
    DataCollector = 'DataCollector'
    DataCurator = 'DataCurator'
    DataManager = 'DataManager'
    Distributor = 'Distributor'
    Editor = 'Editor'
    HostingInstitution = 'HostingInstitution'
    Other = 'Other'
    Producer = 'Producer'
    ProjectLeader = 'ProjectLeader'
    ProjectManager = 'ProjectManager'
    ProjectMember = 'ProjectMember'
    RegistrationAgency = 'RegistrationAgency'
    RegistrationAuthority = 'RegistrationAuthority'
    RelatedPerson = 'RelatedPerson'
    ResearchGroup = 'ResearchGroup'
    RightsHolder = 'RightsHolder'
    Researcher = 'Researcher'
    Sponsor = 'Sponsor'
    Supervisor = 'Supervisor'
    WorkPackageLeader = 'WorkPackageLeader'


class FunderIdentifierTypeEnum(Enum):
    ISNI = 'ISNI'
    GRID = 'GRID'
    Other = 'Other'
    CrossrefFunderID = 'Crossref Funder ID'


class RelatedIdentifierTypeEnum(Enum):
    ARK = 'ARK'
    arXiv = 'arXiv'
    bibcode = 'bibcode'
    DOI = 'DOI'
    EAN13 = 'EAN13'
    EISSN = 'EISSN'
    Handle = 'Handle'
    IGSN = 'IGSN'
    ISBN = 'ISBN'
    ISSN = 'ISSN'
    ISTC = 'ISTC'
    LISSN = 'LISSN'
    LSID = 'LSID'
    PMID = 'PMID'
    PURL = 'PURL'
    UPC = 'UPC'
    URL = 'URL'
    URN = 'URN'


class RelatedIdentifierRelationTypeEnum(Enum):
    IsCitedBy = 'IsCitedBy'
    Cites = 'Cites'
    IsSupplementTo = 'IsSupplementTo'
    IsSupplementedBy = 'IsSupplementedBy'
    IsContinuedBy = 'IsContinuedBy'
    Continues = 'Continues'
    IsDescribedBy = 'IsDescribedBy'
    Describes = 'Describes'
    HasMetadata = 'HasMetadata'
    IsMetadataFor = 'IsMetadataFor'
    HasVersion = 'HasVersion'
    IsVersionOf = 'IsVersionOf'
    IsNewVersionOf = 'IsNewVersionOf'
    IsPreviousVersionOf = 'IsPreviousVersionOf'
    IsPartOf = 'IsPartOf'
    HasPart = 'HasPart'
    IsReferencedBy = 'IsReferencedBy'
    References = 'References'
    IsDocumentedBy = 'IsDocumentedBy'
    Documents = 'Documents'

    IsCompiledBy = 'IsCompiledBy'
    Compiles = 'Compiles'
    IsVariantFormOf = 'IsVariantFormOf'
    IsOriginalFormOf = 'IsOriginalFormOf'
    IsIdenticalTo = 'IsIdenticalTo'
    Reviews = 'Reviews'
    IsReviewedBy = 'IsReviewedBy'
    IsDerivedFrom = 'IsDerivedFrom'
    IsSourceOf = 'IsSourceOf'
    IsRequiredBy = 'IsRequiredBy'
    Requires = 'Requires'


class ResourceTypeEnum(Enum):
    Audiovisual = 'Audiovisual'
    Collection = 'Collection'
    DataPaper = 'DataPaper'
    Dataset = 'Dataset'
    Event = 'Event'
    Image = 'Image'
    InteractiveResource = 'InteractiveResource'
    Model = 'Model'
    PhysicalObject = 'PhysicalObject'
    Service = 'Service'
    Software = 'Software'
    Sound = 'Sound'
    Text = 'Text'
    Workflow = 'Workflow'
    Other = 'Other'
