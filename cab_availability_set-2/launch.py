from flask import Flask, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from config import constants
from werkzeug.datastructures import FileStorage
from error_handler.error_handler import InternalServerError, JsonSyntaxError, SuccessResponse
from utils.logger import create_error_log
from utils.util import store_to_db, get_id, update_location, get_cabs

import os

# Creating Flask App Variable
app = Flask(__name__)
api = Api(app)

arg_parser = reqparse.RequestParser()
arg_parser.add_argument('name')
arg_parser.add_argument('car_number')
arg_parser.add_argument('phone_number')
arg_parser.add_argument('license_number')
arg_parser.add_argument('email')
arg_parser.add_argument('coordinates')


class CabManagement(Resource):
    def post(self):
        try:
            args = arg_parser.parse_args()
            name = args[constants.NAME]
            car_number = args[constants.CAR_NUMBER]
            phone_number = args[constants.PHONE_NUMBER]
            license_number = args[constants.LICENSE_NUMBER]
            email = args[constants.EMAIL]

            if name == "" or car_number == "" or phone_number == "" or license_number == "" or email == "":
                return make_response(jsonify(JsonSyntaxError().to_json()))

            info_json = {}
            info_json[constants.NAME] = name
            info_json[constants.CAR_NUMBER] = car_number
            info_json[constants.PHONE_NUMBER] = phone_number
            info_json[constants.LICENSE_NUMBER] = license_number
            info_json[constants.EMAIL] = email
            info_json[constants.ID] = get_id()
            info_json[constants.LAT] = ""
            info_json[constants.LONG] = ""


            status = store_to_db(info_json)
            if status == True:
                return make_response(jsonify({"msg": constants.REG_SUCCESS, "registered info": info_json}))
            elif status == "duplicate":
                return make_response(jsonify({"msg": constants.DUPLICATE}))

        except Exception as e:
            create_error_log("error in registration" + str(e))
            return make_response(jsonify(InternalServerError().to_json()))


class LocationUpdate(Resource):
    def post(self,driver_id):
        try:
            args = arg_parser.parse_args()
            coordinates = args['coordinates']

            if coordinates == "":
                return make_response(jsonify(JsonSyntaxError().to_json()))

            if "," in str(coordinates):
                filtered_coordinates = coordinates.split(",")
                lat, long = float(filtered_coordinates[0]), float(filtered_coordinates[1])
                status = update_location(driver_id, lat, long)
                
                if status == True:
                    return make_response(jsonify({"msg": constants.LOC_UPDATED, "coordinates": coordinates}))
                else:
                    return make_response(jsonify(InternalServerError().to_json()))
            else:    
                return make_response(jsonify({"msg": constants.INC_COORD}))
            
            
        except Exception as e:
            create_error_log("error in location update" + str(e))
            return make_response(jsonify(InternalServerError().to_json()))


class SearchCabs(Resource):
    def post(self):
        try:
            args = arg_parser.parse_args()
            coordinates = args['coordinates']
            
            if coordinates == "":
                return make_response(jsonify(JsonSyntaxError().to_json()))
            
            if "," in str(coordinates):
                filtered_coordinates = coordinates.split(",")
                lat, long = float(filtered_coordinates[0]), float(filtered_coordinates[1])
                status, count = get_cabs(lat, long)
                
                if status == True:
                    
                    if count != 0:
                        return make_response(jsonify({"nearby cabs": count}))
                    else:
                        return make_response(jsonify({"msg": constants.NO_CABS}))
                
                else:
                    return make_response(jsonify(InternalServerError().to_json()))
            else:    
                return make_response(jsonify({"msg": constants.INC_COORD}))
            
            
        except Exception as e:
            create_error_log("error in post function" + str(e))
            return make_response(jsonify(InternalServerError().to_json()))


api.add_resource(CabManagement, '/api/v1/driver/register')
api.add_resource(LocationUpdate, '/api/v1/<string:driver_id>/updateLocation')
api.add_resource(SearchCabs, '/api/v1/cabs/search')

if __name__ == "__main__":
    app.run(debug=True)
