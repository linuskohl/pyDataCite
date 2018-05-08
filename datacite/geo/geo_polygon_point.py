from marshmallow import Schema, fields, ValidationError, pre_load, post_load


class PolygonPoint(object):
    '''PolygonPoint object'''

    def __init__(self, pointLongitude, pointLatitude):
        self.pointLongitude = pointLongitude
        self.pointLatitude = pointLatitude


class PolygonPointSchema(Schema):
    '''PolygonPoint object schema'''

    # Longitudinal dimension of point
    pointLongitude = fields.Float(required=True)
    # Latitudinal dimension of point
    pointLatitude = fields.Float(required=True)

    @post_load
    def make_polygon_point(self, data):
        '''Return PolygonPoint object after loading'''
        return PolygonPoint(**data)
