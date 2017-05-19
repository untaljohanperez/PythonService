from flask_restful import Resource
from datetime import datetime
from datetime import timedelta

class Overload(Resource):
    def overLoad(self, seconds):
        waitTill = datetime.now() + timedelta(seconds=seconds)
        while (waitTill > datetime.now()):
            print (datetime.now())

    def get(self):
        self.overLoad(5)
        return { 
            'time': str(datetime.now())
        }