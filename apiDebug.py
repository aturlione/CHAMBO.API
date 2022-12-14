from flask import Flask
from flask_restx import Api
import geo_process

app = Flask(__name__, instance_relative_config=True)
apiflask = Api(app, version="0.0.1", title="CHAMBO API")

geo_process.start(apiflask)