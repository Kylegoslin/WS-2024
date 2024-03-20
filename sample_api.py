from flask import Flask
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

class GetProducts(Resource):
    def get(self):
        return {'id': '1221'}
        
 
             
api.add_resource(GetProducts, '/getProducts')



class GetRootPage(Resource):
    def get(self):
        return {'hello': 'root'}
        
 
             
api.add_resource(GetRootPage, '/')


            
if __name__ == '__main__':
    app.run(debug=True)
