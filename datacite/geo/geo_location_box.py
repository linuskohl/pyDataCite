from marshmallow import Schema, fields, ValidationError, pre_load, post_load


class GeoLocationBox(object):
    '''The spatial limits of a box'''

    def __init__(self, westBoundLongitude, eastBoundLongitude, southBoundLatitude, northBoundLatitude):
        self.westBoundLongitude = westBoundLongitude
        self.eastBoundLongitude = eastBoundLongitude
        self.southBoundLatitude = southBoundLatitude
        self.northBoundLatitude = northBoundLatitude


class GeoLocationBoxSchema(Schema):
    '''Schema of the spatial limits of a box'''

    """Western longitudinal dimension of box"""
    westBoundLongitude = fields.Float(required=True)
    # Eastern longitudinal dimension of box
    eastBoundLongitude = fields.Float(required=True)
    # Southern longitudinal dimension of box
    southBoundLatitude = fields.Float(required=True)
    # Northern longitudinal dimension of box
    northBoundLatitude = fields.Float(required=True)

    @post_load
    def make_geo_location_box(self, data):
        '''Return GeoLocationBox object after loading'''
        return GeoLocationBox(**data)
