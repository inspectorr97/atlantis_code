from geopy.distance import geodesic

# function to extract clean latitude, longitude of city


def get_filtered_coordinates(city):
    try:
        coordinates = str(city).split(",")
        lat, long = coordinates[0], coordinates[1]

        if "N" in str(lat).upper():
            lat = float(str(lat).replace("N", "").strip())

        elif "S" in str(lat).upper():
            lat = float("-" + str(lat).replace("S", "").strip())

        if "E" in str(long).upper():
            long = float(str(long).replace("E", "").strip())

        elif "W" in str(long).upper():
            long = float("-" + str(long).replace("W", "").strip())

        return (lat, long)
    except Exception as e:
        print("Exception occured while filtering coordinates: ", e)

# function to find distance between the 2 cities


def get_distance(city1, city2):
    try:
        coordinates_city1 = get_filtered_coordinates(city1)
        coordinates_city2 = get_filtered_coordinates(city2)

        # Print the distance calculated in km
        distance = geodesic(coordinates_city1, coordinates_city2).km

        return distance

    except Exception as e:
        print("couldn't complete request due to : ", e)


if __name__ == "__main__":
    City1 = input("City1: ")
    City2 = input("City2: ")
    if City1 == "" or City2 == "":
        print("incorrect coordinates input")
    else:
        distance = get_distance(City1, City2)
        print(f"City 1 and City 2 are {distance} km apart")
