from flask import Flask, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from config import constants
from werkzeug.datastructures import FileStorage
from error_handler.error_handler import InternalServerError, JsonSyntaxError, SuccessResponse
from utils.logger import create_error_log
from utils.to_csv import create_csv

import os

# Creating Flask App Variable
app = Flask(__name__)
api = Api(app)

arg_parser = reqparse.RequestParser()
# arg_parser.add_argument('url')
arg_parser.add_argument('file', type=FileStorage,
                        location='files', action='append')


def allowed_file(filename):
    ALLOWED_EXT = constants.ALLOWED_EXTENSIONS
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT


class WebsiteScraping(Resource):
    def post(self):
        try:
            args = arg_parser.parse_args()
            upload_file_list = args['file']
            # configure file upload folder
            file_root = os.path.realpath(os.path.dirname(__file__))
            app.config['UPLOAD_FOLDER'] = os.path.join(
                file_root, constants.TEMP)
            # save file to upload folder
            valid_files = []
            invalid_files = []
            for file in upload_file_list:
                if allowed_file(file.filename):
                    filename = file.filename
                    file.save(os.path.join(
                        app.config['UPLOAD_FOLDER'], filename))
                    filepath = os.path.join(
                        app.config['UPLOAD_FOLDER'], filename)
                    valid_files.append(filepath)
                else:
                    print("in else part")
                    invalid_files.append(file.filename)

            if len(invalid_files) > 0:
                return make_response(jsonify(JsonSyntaxError().to_json()))

            status = create_csv(filepath)

            if status:
                return make_response(jsonify(SuccessResponse().to_json()))
            else:
                return make_response(jsonify(InternalServerError().to_json()))

        except Exception as e:
            create_error_log(e)
            return make_response(jsonify(InternalServerError().to_json()))


api.add_resource(WebsiteScraping, '/upload')

if __name__ == "__main__":
    app.run(debug=True)
