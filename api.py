# Products Service 

from flask import Flask
from flask_restful import Api
from resources.product import Product
from resources.home import Home
from resources.overload import Overload
from resources.user import User

app = Flask(__name__)
api = Api(app)
		      
api.add_resource(Home, '/')
api.add_resource(Product, '/product')
api.add_resource(Overload, '/overload')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)



