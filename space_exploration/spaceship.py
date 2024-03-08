import random
import time


class spaceship:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.health = 100
        self.last_updated_time = 0

    def __str__(self):
        return f'Spaceship name: {self.name} ,Health: {self.health}, fuel {self.fuel}'

    def update_fuel(self):
        curr_time = time.time()
        time_diff = curr_time - self.last_updated_time
        self.fuel -= int(time_diff) / 10
        self.last_updated_time = curr_time

    def launch_spaceship(self):
        self.last_updated_time = time.time()
        print(f"{self.name} is launching into space!")

    def explore_galaxy(self, events):
        random_event = random.choice(events)

        if len(random_event.deal_options) == 2 and 'health' not in random_event.deal_options.keys():
            print(f"\n{self.name} faced: {random_event.name}")
            options = list(random_event.deal_options.keys())
            curr_time = time.time()
            decision = input(f"Do you want to {options[0]} or {options[1]} ? ")
            while decision not in options:
                decision = input(f"Invalid choice,Do you want to {options[0]} or {options[1]} ? ")
                if int(time.time() - curr_time) > 5:
                    print("Invalid choice. The spaceship takes damage due to indecision.")
                    self.health -= 5
                    decision = None
                    break
        else:
            if len(random_event.deal_options) == 2:
                print(f"{self.name} encountered friendly aliens.")
                curr_time = time.time()
                decision = input('They provide assistance,Do you want health or fuel assistance? ')
                while decision != 'health' and decision != 'fuel':
                    decision = input(f"Invalid choice,Do you want health or fuel assistance? ")
                    if int(time.time() - curr_time) > 5:
                        print("Timeout!! aliens left")
                        decision = None
                        break
            else:
                decision = "black hole"
        if decision != None:
            random_event.event_factory_print(decision, self)()
            health_update, fuel_update = random_event.calculate_damage_or_assist(decision)
            self.health += health_update
            self.fuel += fuel_update
