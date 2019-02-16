from flask import Flask
from flask_restful import Api, Resource, reqparse
import requests
import json

app = Flask(__name__)
api = Api(app)



class Business(Resource):
    def get(self, location, term):
        apikey = 'Npl1NETZn9_gAG-Rt8a-8c9-KgFsgwADqzDzMrI-mJkogKlt5hDnXsm6GUvxnagexoZY4i5uiB9gVrlodOeT9ON3Yf_cEn-l8XuKNPycMNbtx6gXJBzIOWkxVgdoXHYx'
        url = 'https://api.yelp.com/v3/businesses/search'
        headers = {'Authorization':'Bearer {}'.format(apikey)}
        para = {'location':location, 'categories':term, 'limit':5}

        req = requests.get(url, headers=headers, params=para)
        jdata = json.loads(req.text)

        return jdata, req.status_code



api.add_resource(Business, "/<string:location>/<string:term>")

app.run(debug=True)