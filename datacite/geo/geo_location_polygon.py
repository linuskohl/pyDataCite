from marshmallow import Schema, fields, ValidationError, pre_load, post_load
from .geo_polygon_point import PolygonPointSchema


class GeoLocationPolygon(object):
    def __init__(self, polygonPoints, inPolygonPoint=None):
        self.polygonPoints = polygonPoints
        self.inPolygonPoint = inPolygonPoint


class GeoLocationPolygonSchema(Schema):
    # A point location in a polygon
    polygonPoints = fields.Nested('PolygonPointSchema', many=True, required=True)

    # For any bound area that is larger than half the earth, define a (random) point inside
    inPolygonPoint = fields.Nested('PolygonPointSchema', many=False)

    @post_load
    def make_geo_location_polygon(self, data):
        return GeoLocationPolygon(**data)
