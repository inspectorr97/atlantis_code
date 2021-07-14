import os
import json
from utils.logger import create_error_log
import string
import random
from geopy.distance import geodesic
from config import constants

# function to store data to json


def store_to_db(info):
    try:
        status = True

        info = eval(json.dumps(info))

        with open(constants.JSON_PATH, 'r+') as json_file:
            data = json.load(json_file)

            for entries in data:
                if info[constants.CAR_NUMBER] == entries[constants.CAR_NUMBER] or info[constants.PHONE_NUMBER] == entries[constants.PHONE_NUMBER] or info[constants.LICENSE_NUMBER] == entries[constants.LICENSE_NUMBER] or info[constants.EMAIL] == entries[constants.EMAIL]:
                    status = "duplicate"
                    break
            if status == "duplicate":
                return status
            else:
                data.append(info)
                with open(constants.JSON_PATH, 'w+') as json_file:
                    json_file.seek(0)
                    json.dump(data, json_file)

        return status
    except Exception as e:
        create_error_log("error in store_to_db" + e)
        return False

# function to generate random 6digit id


def get_id():
    # initializing size of string
    str_size = 6

    # generating random strings
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=str_size))

    return res

# function to get filtered coordinates


def get_filtered_coordinates(lat, long):
    try:

        if "N" in str(lat).upper():
            lat = float(str(lat).replace("N", "").strip())

        elif "S" in str(lat).upper():
            lat = float("-" + str(lat).replace("S", "").strip())

        if "E" in str(long).upper():
            long = float(str(long).replace("E", "").strip())

        elif "W" in str(long).upper():
            long = float("-" + str(long).replace("W", "").strip())

        return lat, long
    except Exception as e:
        create_error_log(
            "Exception occured while filtering coordinates: " + str(e))


# function to update driver's location in db


def update_location(driver_id, lat, long):
    try:
        status = "not found"
        driver_lat, driver_long = get_filtered_coordinates(lat, long)
        location = {}
        location['latitude'] = float(str(driver_lat).strip())
        location['longitude'] = float(str(driver_long).strip())
        with open(constants.JSON_PATH, 'r+') as json_file:
            data = json.load(json_file)
            for entry in data:
                if entry["id"] == driver_id:
                    entry.update(location)
                    status = "found"
                    break
        if status == "found":
            with open(constants.JSON_PATH, 'w+') as json_file:
                json_file.seek(0)
                json.dump(data, json_file)
        return True
    except Exception as e:
        create_error_log("error while updating location" + e)
        return False

# function to search nearby cabs


def get_cabs(lat, long):
    try:
        count = 0
        lat, long = get_filtered_coordinates(lat, long)
        with open(constants.JSON_PATH, 'r+') as json_file:
            data = json.load(json_file)
            for entry in data:
                if entry['latitude'] != "" or entry['longitude'] != "":
                    # distance calculated in km
                    distance = geodesic(
                        (entry['latitude'], entry['longitude']), (lat, long)).km
                    if distance <= 4:
                        count += 1

        return True, count

    except Exception as e:
        create_error_log("couldn't get distance due to : " + e)
        return False
