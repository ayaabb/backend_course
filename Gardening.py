class plant:
    def __init__(self, name, sun1_or_rain2, water, wind):
        self.name = name
        self.sun1_or_rain2 = sun1_or_rain2
        self.water = water
        self.wind = wind
        self.max_snow = 0

    def add_max_snow(self, max_snow):
        self.max_snow = max_snow


if __name__ == '__main__':
    plant1 = plant("rose", 2, 50, True)
    plant2 = plant("ash", 1, 10, False)
    plant3 = plant("Magnolia", 1, 100, True)

    weather = int(input("Describe the weather today:\nIts cloudy or sunny? 1.sunny 2.cloudy \n"))
    water = int(input("What is the precipitation number? "))
    wind = True if input("Is there wind? Yes or No\n") is 'Yes' else False

    print("Plants which like the weather today are: ")
    if plant1.sun1_or_rain2 == weather:
        print(plant1.name + ' ')
    if plant2.sun1_or_rain2 == weather:
        print(plant2.name + ' ')
    if plant3.sun1_or_rain2 == weather:
        print(plant3.name + ' ')

    print("Plants which like the precipitation today are: ")
    if plant1.water == water:
        print(plant1.name+ ' ')
    if plant2.water == water:
        print(plant2.name + ' ')
    if plant3.water == water:
        print(plant3.name + ' ')

    print("Plants which like the wind condition today are: ")
    if plant1.wind == wind:
        print(plant1.name + ' ')
    if plant2.wind == wind:
        print(plant2.name + ' ')
    if plant3.wind == wind:
        print(plant3.name + ' ')

    plant1.add_max_snow(20)
    plant2.add_max_snow(40)
    plant3.add_max_snow(100)

    snow = int(input("What is the snow amount today? "))
    print("Plants which will die because of the snow today are: ")
    if plant1.max_snow <= snow:
        print(plant1.name + ' ')
    if plant2.max_snow <= snow:
        print(plant2.name + ' ')
    if plant3.max_snow <= snow:
        print(plant3.name + ' ')
