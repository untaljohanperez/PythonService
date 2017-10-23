from flask_restful import Resource
import platform

class Home(Resource):
    def get(self):
        return {
            'host': platform.node()
        }