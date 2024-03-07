import json
import requests


def get_and_save_data(url_nasa, key):  # requesting data and saving it in json file
    response = requests.get(url_nasa + key).json()
    with open("asteroids.json", "w") as file:
        json.dump(response, file)

    return response


def get_details(data):  # processing the data and saving the required details
    asteroid_data = []
    for date in data:
        for asteroid in data[date]:
            asteroid_info = {
                'id': asteroid['id'],
                'name': asteroid['name'],
                'est_diameter_min': asteroid['estimated_diameter']['kilometers']['estimated_diameter_min'],
                'est_diameter_max': asteroid['estimated_diameter']['kilometers']['estimated_diameter_max'],
                'miss_distance_KM': float(asteroid['close_approach_data'][0]['miss_distance']['kilometers']),
                'relative_velocity_KMH': float(
                    asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
            }
            asteroid_data.append(asteroid_info)
    return asteroid_data
