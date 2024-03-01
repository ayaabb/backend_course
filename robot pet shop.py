import random
import names


class robot:
    def __init__(self, name, id, battery_type):
        self.name = name
        self.id = id
        self.battery_type = battery_type


class pet_robot(robot):
    def __init__(self, name, id, battery_type, main_material, price, cost_to_fix_per_day, animal_type, status):
        self.main_material = main_material
        self.price = price
        self.cost_to_fix_per_day = cost_to_fix_per_day
        self.animal_type = animal_type
        self.status = status
        if status == 'in repair' or status == 'to be shipped':
            self.days_for_status = random.randint(1, 3)
        else:
            self.days_for_status = 0
        super().__init__(name, id, battery_type)

    def print_pet(self):
        print(self.__dict__)


class employee_robot(robot):
    def __init__(self, name, id, battery_type, daily_salary):
        self.daily_salary = daily_salary
        super().__init__(name, id, battery_type)


class robot_pet_shop:
    def __init__(self):
        self.pets = []
        self.name_to_id = {}
        self.employees = []
        self.balance = 0

    def print_pets_by_status(self, status, price_range):

        if price_range[1] == 0:
            print(f"{status} pets :")
        else:
            print(f"Available pets {status} based on {price_range} are :")
        for p in self.pets:
            if p.status == status:
                if price_range[1] != 0:
                    if price_range[0] <= p.price <= price_range[1]:
                        print(p.name)
                else:
                    print(p.name)
        print('')

    def print_salaries(self):
        print("Employees salaries :")
        for emp in self.employees:
            print(f"{emp.name}'s daily salary is {emp.daily_salary}")

    def sell(self, pet):
        self.balance += pet.price
        pet.status = 'to be shipped'
        pet.days_for_status = random.randint(1, 3)

    def print_details(self, name_or_id):
        if isinstance(name_or_id, int):
            pet = self.pets[name_or_id - 1]

        else:
            pet = self.pets[self.name_to_id[name_or_id]]

        return pet

    def repair(self, pet):
        pet.status = 'in repair'
        pet.days_for_status = random.randint(1, 3)

    def update_balance_per_day(self):
        for emp in self.employees:
            self.balance -= emp.daily_salary
        for p in self.pets:
            if p.status == 'in repair':
                p.days_for_status -= 1
                self.balance -= p.cost_to_fix_per_day
                if p.days_for_status == 0:
                    p.status = 'for sale'
            if p.status == 'to be shipped':
                p.days_for_status -= 1
                if p.days_for_status == 0:
                    p.status = 'sold'


battery_type_list = ['lithium', 'alkaline']
animal_type_list = ['herbivore', 'carnivore']
main_material_list = ['iron', 'steel', 'plastic']
status_list = ['for sale', 'broken', 'in repair', 'to be shipped', 'sold']
animal_names = ['Dog 1', 'Cow 0', 'Cat 1', 'Horse 0', 'Tiger 1', 'Lion 1', 'cheetah 1', 'robot 0', 'sheep 0', 'bear 1']
our_shop = robot_pet_shop()

for i in range(10):
    our_shop.pets.append(pet_robot(animal_names[i].split()[0], i + 1, random.choice(battery_type_list),
                                   random.choice(main_material_list),
                                   random.randint(50, 200), random.randint(2, 10),
                                   animal_type_list[int(animal_names[i].split()[1])], random.choice(status_list)))
    our_shop.name_to_id[animal_names[i].split()[0]] = i
    if our_shop.pets[i].status == 'sold':
        our_shop.balance += our_shop.pets[i].price

for i in range(3):
    our_shop.employees.append(
        employee_robot(names.get_full_name(), i + 1, random.choice(battery_type_list), random.randint(5, 20)))

our_shop.print_pets_by_status('for sale', (0, 0))
our_shop.print_pets_by_status('in repair', (0, 0))
our_shop.print_pets_by_status('for sale', (50, 100))
our_shop.print_salaries()
print(f'Store balance = {our_shop.balance} ')
answer='yes'
while answer == 'yes':
    our_shop.print_pets_by_status('for sale', (0, 0))
    answer = input("Do you want to sell a robot pet ?")
    while answer != "yes" and answer != "no":
        answer = input("Invalid input try again,Do you want to sell robot pet ?")
    if answer=='no':
        break
    pet = input("Choose pet to sell:")

    while pet not in our_shop.name_to_id.keys():
        pet = input("Invalid input try again,Choose pet to sell?")
    pet_details = our_shop.print_details(pet)
    our_shop.sell(pet_details)
    pet_details.print_pet()
    our_shop.print_pets_by_status('broken', (0, 0))
    repair_answer = input("Do you want to repair a broken robot pet ?")
    while repair_answer != "yes" and repair_answer != "no":
        repair_answer = input("Invalid input try again,Do you want to repair a broken robot pet ?")
    if repair_answer == 'yes':
        pet = input("Choose pet to repair:")
        while pet not in our_shop.name_to_id.keys():
            pet = input("Invalid input try again,Choose pet to repair:")
        pet_status = our_shop.print_details(pet).status
        while pet_status != 'broken':
            pet = input("This pet is not broken,Choose pet to repair:")
            while pet not in our_shop.name_to_id.keys():
                pet = input("Invalid input try again,Choose pet to repair:")
            pet_status = our_shop.print_details(pet).status
        our_shop.repair(our_shop.print_details(pet))
        our_shop.print_details(pet).print_pet()

    our_shop.update_balance_per_day()
    print(f'Store balance = {our_shop.balance} ')
our_shop.print_pets_by_status('sold',(0,0))

