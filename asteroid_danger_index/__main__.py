from calculating_index_danger import *
from scrape_data import *

from plotting_data import *

api_key = open('asteroid_danger_index/api_key.txt')
api_key = api_key.read()
data = get_and_save_data('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-09&api_key=',
                         api_key)
asteroids = get_details(data['near_earth_objects'])
plot_graph(asteroids, 'est_diameter_min', 'relative_velocity_KMH')
plot_graph(asteroids, 'miss_distance_KM', 'est_diameter_max')
A, B, C = ask_for_ABC_values()
danger_index_list = calculate_danger(asteroids, A, B, C)
names = [ast['name'] for ast in asteroids]
plot_barChart(danger_index_list, names)
