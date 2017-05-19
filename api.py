# Products Service 

from flask import Flask
from flask_restful import Resource, Api
from product import Product
from overload import Overload

app = Flask(__name__)
api = Api(app)
		      
api.add_resource(Product, '/')
api.add_resource(Overload, '/overload')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)



