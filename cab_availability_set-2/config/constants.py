#logs details
LOG_FOLDERNAME = 'logs'
LOG_FILENAME = 'error_log.txt'

#info constants
NAME = "name"
CAR_NUMBER = "car_number"
PHONE_NUMBER = "phone_number"
LICENSE_NUMBER = "license_number"
EMAIL = "email"
ID = "id"
LAT = "latitude"
LONG = "longitude"

#custom messages
REG_SUCCESS = "Registered successfully!"
DUPLICATE = "Data already present, please add unique info for fields other than name"
LOC_UPDATED = "Location updated"
INC_COORD = "Incorrect coordinates input"
NO_CABS = "no cabs available at the moment!"

#database json path
import os
JSON_PATH = os.path.join(os.getcwd(), "storage", "db.json")


