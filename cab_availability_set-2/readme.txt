1. To register as a driver give POST request to http://127.0.0.1:5000/api/v1/driver/register
giving the following parameters as an input :
name (str),
car_number (str),
phone_number (str),
license_number(str),
email (str)

sample input (Postman -> body -> form-data) :
name - Rishabh
car_number - DL9CM2739
phone_number - 8527281232
license_number - DL1Y456788
email - sharmarishabh121@gmail.com

NOTE : save the generated id somewhere, as it will be used to update the location

2. To update driver's location give POST request to http://127.0.0.1:5000/api/v1/driver_id/updateLocation
giving the following parameter as an input : 
coordinates (type str - separated with a coma(,))

3. To search for nearby cabs give a POST request to http://127.0.0.1:5000/api/v1/cabs/search
giving the following paramter as an input : 
coordinates (type str - separated with a coma(,))

Status code and their meanings:

when a 500 code is returned it indicates an unknown error has come
up, reach out to the provider to resolve the issue or check the logs.

when a 400 code is returned it indicates a json syntax error which is usually from the user end
check and verify the inputs, if error still persists check the logs.
XXXXXXXXXXXX---END---XXXXXXXXXXXX
