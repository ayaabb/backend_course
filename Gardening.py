import random


class plant:
    def __init__(self, name, sun_or_rain, water, wind):
        self.name = name
        self.sun_or_rain = sun_or_rain
        self.water = water
        self.wind = wind
        self.max_snow = 0


def check_ifPlantsLikeConditions(plants, conditions):
    for i in range(len(conditions)):
        list_liked_plants = []
        for plant in plants:
            if (i == 0 and plant.sun_or_rain == conditions[i]) or (i == 2 and plant.wind == conditions[i]):
                list_liked_plants.append(plant.name)
            if i == 1 and plant.water // 1.5 <= conditions[
                i] <= 1.5 * plant.water:  # plant water need=X , X/1.5=<suitable amount of water<=X*1.5
                list_liked_plants.append(plant.name)
        if i == 0:
            if len(list_liked_plants) > 0:
                print(f"The plants which like the weather today are: {list_liked_plants}\n")
            else:
                print(f"There is no plants that like the weather today\n")
        if i == 1:
            if len(list_liked_plants) > 0:
                print(f"The plants which the amount of water today is suitable for them are: {list_liked_plants}\n")
            else:
                print(f"The amount of water today is not suitable for any plant\n")
        if i == 2:
            if len(list_liked_plants) > 0:
                print(f"The plants which like the wind condition today are: {list_liked_plants}\n")
            else:
                print(f"There is no plants that like the wind condition today\n")


def check_DeadPlants(plants, snow_Amount):
    dead_plants = []
    for plant in plants:
        if plant.max_snow <= snow_Amount:
            dead_plants.append(plant.name)
    if len(dead_plants) > 0:
        print(f"Plants which will die because of the snow today are: {dead_plants}\n")
    else:
        print(f"There is no plants that will die today because of the snow\n")


if __name__ == '__main__':
    names = ["rose", "ash", "Magnolia"]
    plants = []
    for i in range(3):
        plants.append(plant(names[i], random.randint(1, 2), random.randint(1, 100), random.randint(1, 2)))

    weather = input("Describe the weather today:\nIts cloudy or sunny? press 1 for 'sunny' or  2 for 'cloudy' \n")
    while not weather.isdigit() or (int(weather) != 1 and int(weather) != 2):
        weather = (input("Invalid input,try again \nIts cloudy or sunny? press 1 for 'sunny' or  2 for 'cloudy' \n"))
    weather = int(weather)

    water = input("What is the precipitation number? choose number in range 1-100:")
    while not water.isdigit() or int(water) < 0 or int(water) > 100:
        water = input("Invalid input, try again \nWhat is the precipitation number? choose number in range 1-100:")
    water = int(water)

    wind = (input("Is there a wind? press 1 for 'Yes' or  2 for 'No'\n"))
    while not wind.isdigit() or (int(wind) != 1 and int(wind) != 2):
        wind = (input("Invalid input, try again \nIs there a wind? press 1 for 'Yes' or  2 for 'No'\n"))
    wind = int(wind)

    conditions = [weather, water, wind]
    check_ifPlantsLikeConditions(plants, conditions)

    for plant in plants:
        plant.max_snow = random.randint(1, 100)

    snow = input("What is the snow amount today?  choose number in range 1-100:")
    while not snow.isdigit() or int(snow) < 0 or int(snow) > 100:
        snow = input("Invalid input, try again \nWhat is the snow amount today?  choose number in range 1-100:")
    snow = int(snow)

    check_DeadPlants(plants, snow)
