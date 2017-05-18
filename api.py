# Products Service 

from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime
from datetime import timedelta

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'products': ['Ice Cream',
                        'Chocolate',
                        'Morcilla',
                        'Fruit']
        }
		
class Overload(Resource):
    def overLoad(self, seconds):
        waitTill = datetime.now() + timedelta(seconds=seconds)
        while (waitTill > datetime.now()):
            print (datetime.now())

    def get(self):
        self.overLoad(5)
        return { 
            'time': datetime.now() 
        }
        
api.add_resource(Product, '/')
api.add_resource(Overload, '/overload')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)



