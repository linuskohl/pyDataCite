from marshmallow import Schema, fields, ValidationError, pre_load, post_load


# Subject, keywords, classification codes, or key phrases describing the resource

class Subject(object):
    def __init__(self, subject=None, subjectScheme=None, valueURI=None, schemeURI=None, lang=None):
        self.subject = subject
        self.subjectScheme = subjectScheme
        self.valueURI = valueURI
        self.schemeURI = schemeURI
        self.lang = lang


class SubjectSchema(Schema):
    subject = fields.String()
    subjectScheme = fields.String()
    valueURI = fields.Url()
    schemeURI = fields.Url()
    lang = fields.String()

    @post_load
    def make_subject(self, data):
        return Subject(**data)
