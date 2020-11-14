from flask import json
from flask_restful import Resource
from marshmallow import Schema, fields
from webargs.flaskparser import use_args
from db import mongo
from util import mongo_id_decoder, validate_stock_id


class GetSchema(Schema):
    _id = fields.Function(deserialize=mongo_id_decoder)
    companyName = fields.Str()
    symbol = fields.Str()

class Stock(Resources):
    @use_args(GetSchema(), location="querystring")
    def get(self, query):
        # Search for all users that match query arguments
        users = [user for user in mongo.db.user.find(query)]
        return json.jsonify(data=users)