import asyncio
import json
import aiofiles
import aiohttp


async def run_parallel(
        parameters_list):  # creating asynchronous tasks for each set of parameters of each week and run them concurrently
    async with aiohttp.ClientSession() as session:  # create an asynchronous HTTP client session
        tasks = [asyncio.create_task(get_and_save_data(session, *params)) for params in
                 parameters_list]
        data_weeks_list = await asyncio.gather(*tasks)
    return data_weeks_list


async def get_and_save_data(session, url_nasa_key,
                            week_number):  # making an asynchronous web request of a specific week and save the data to a file
    print('save data week' + week_number + ' started')
    async with session.get(url_nasa_key) as response:
        data = await response.json()

    async with aiofiles.open(f'week{week_number}.json', 'w') as file:
        await file.write(json.dumps(data))
    print('week' + week_number + ' ended')
    return data


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


def week_url(url, week_num, year_and_month, api_key):  # creating a URL of a specific week
    first_day = (week_num - 1) * 7 + 1
    last_day = first_day + 6
    if first_day < 10:
        first_day = '0' + str(first_day)
    else:
        first_day = str(first_day)
    if last_day < 10:
        last_day = '0' + str(last_day)
    else:
        last_day = str(last_day)
    return url + 'start_date=' + year_and_month + first_day + '&end_date=' + year_and_month + last_day + '&api_key=' + api_key
