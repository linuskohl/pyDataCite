from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from .geo.geo_location_box import GeoLocationBoxSchema
from .geo.geo_location_polygon import GeoLocationPolygonSchema
from .geo.geo_polygon_point import PolygonPointSchema


class GeoLocation(object):
    '''GeoLocation object'''

    def __init__(self, geoLocationPoint=None, geoLocationBox=None, geoLocationPlace=None, geoLocationPolygon=None,
                 geoLocationPolygons=None):
        self.geoLocationPoint = geoLocationPoint
        self.geoLocationBox = geoLocationBox
        self.geoLocationPlace = geoLocationPlace
        self.geoLocationPolygon = geoLocationPolygon
        self.geoLocationPolygons = geoLocationPolygons


class GeoLocationSchema(Schema):
    '''GeoLocation object schema'''
    # A point location in space
    geoLocationPoint = fields.Nested('PolygonPointSchema', many=False)
    # The spatial limits of a box
    geoLocationBox = fields.Nested('GeoLocationBoxSchema', many=False)
    # Spatial region or named place where the data was gathered or about which the data is focused
    geoLocationPlace = fields.String()
    # WARNING: This field has been superseded by 'geoLocationPolygons'
    geoLocationPolygon = fields.Nested('GeoLocationPolygonSchema', many=True)
    # A drawn polygon area, defined by a set of points and lines connecting the points in a closed chain.
    geoLocationPolygons = fields.Nested('GeoLocationPolygonSchema', many=True)

    @post_load
    def make_geo_location(self, data):
        '''Retrun GeoLocation object after loading'''
        return GeoLocation(**data)
