from flask_restful import Resource
from database.connection import database

users_collection = database.users

class User(Resource):
    def get(self):
        return users_collection.find_one()