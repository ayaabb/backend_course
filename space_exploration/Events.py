import random

class Event:
    def __init__(self, name, deal_options):
        self.name = name
        self.deal_options = deal_options

    def calculate_damage_or_assist(self, decision):
        health_update = 0
        fuel_update = 0
        if decision != 'health' and decision != 'fuel' and decision != 'black hole':
            options = self.deal_options[decision]
        else:
            options = self.deal_options

        if decision != 'fuel' and 'health' in options.keys():
            health_update = random.randint(options['health'][0],
                                           options['health'][1])
            if health_update < 0:
                print(f'took {health_update} health damage', end=' ')
            else:
                print(f"the spaceship's health increased by {health_update} ")
        if decision != 'health' and 'fuel' in options:
            fuel_update = random.randint(options['fuel'][0], options['fuel'][1])
            if fuel_update < 0:
                print(f'consume {fuel_update} fuel ', end=' ')
            else:
                print(f"the spaceship's fuel increased by {fuel_update} ")

        print('\n')
        return health_update, fuel_update

    def event_factory_print(self, decision, spaceship):
        def asteroid_field_event():
            if decision == 'evade':
                print(f"{spaceship.name} successfully evaded the asteroid field.")
            elif decision == 'fire':
                print(f"{spaceship.name} fired at the asteroids.")

        def space_pirates_event():
            if decision == 'negotiate':
                print(f"{spaceship.name} successfully negotiated with the space pirates.")
            elif decision == 'fight':
                print(f"{spaceship.name} engaged in a battle with space pirates.")

        def black_hole_event():
            print(f"{spaceship.name} is caught in a black hole.")

        if self.name == "Asteroid Field":
            return asteroid_field_event
        elif self.name == "Space Pirates":
            return space_pirates_event
        elif self.name == "Black Hole":
            return black_hole_event
