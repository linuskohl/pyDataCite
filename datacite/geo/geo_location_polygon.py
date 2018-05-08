from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from .geo_polygon_point import PolygonPointSchema
from numbers import *


class GeoLocationPolygon(object):
    '''GeoLocationPolygon object'''

    def __init__(self, polygonPoints, inPolygonPoint=None):
        self.polygonPoints = polygonPoints
        self.inPolygonPoint = inPolygonPoint


class GeoLocationPolygonSchema(Schema):
    '''GeoLocationPolygon object schema'''

    # A point location in a polygon
    polygonPoints = fields.Nested('PolygonPointSchema', many=True, required=True)
    # For any bound area that is larger than half the earth, define a (random) point inside
    inPolygonPoint = fields.Nested('PolygonPointSchema', many=False)

    @post_load
    def make_geo_location_polygon(self, data):
        '''Return GeoLocationPolygon object after loading'''
        return GeoLocationPolygon(**data)
