from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import sys, os

import time

from test import execute
from generate_cardiac_features_test import execute_generate_features_test
from stage_1_diagnosis import diagnosis_stage_1
from stage_2_diagnosis import diagnosis_stage_2

app = Flask(__name__)
api = Api(app)


"""def this_funct():
    return "okee"""
    
class Prediction(Resource):

    def get(self):
        start_time = time.time()
        execute()
        execute_generate_features_test()
        diagnosis_stage_1()
        diagnosis_stage_2()
        print("--- %s seconds ---" % (time.time() - start_time))
        return {"return json" : "nice"}
    
api.add_resource(Prediction, "/predict")

if __name__ == "__main__":
	app.run(debug=True, threaded=True)