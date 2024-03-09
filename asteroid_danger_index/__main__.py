import time
from calculating_index_danger import *
from scrape_data import *
from plotting_data import *

if __name__ == '__main__':
    url = 'https://api.nasa.gov/neo/rest/v1/feed?'
    api_key = open('api_key.txt')
    api_key = api_key.read()

    url_week_num = []
    for i in range(4):  # creating list of urls for all the weeks
        url_week_num.append((week_url(url, i + 1, '2016-04-', api_key), str(i + 1)))

    start_time = time.time()
    data_list = asyncio.run(run_parallel(url_week_num))
    print(f'The 4 weeks of scraping data in parallel took {format(time.time() - start_time, '.2f')} seconds')
    for i in range(len(data_list)):
        asteroids = get_details(data_list[i]['near_earth_objects'])
        plot_graph(asteroids, 'est_diameter_min', 'relative_velocity_KMH', i + 1)
        plot_graph(asteroids, 'miss_distance_KM', 'est_diameter_max', i + 1)
        A, B, C = ask_for_ABC_values(i + 1)
        danger_index_list = calculate_danger(asteroids, A, B, C)
        names = [ast['name'] for ast in asteroids]
        print(f"The number of asteroids in week{i + 1} is : {len(names)} ")
        plot_barChart(danger_index_list, names, i + 1)
