from collections import defaultdict


class item:
    def __init__(self, weight):
        self.weight = weight


class branded_items(item):
    def __init__(self, weight, brand):  # charger,sneakers,smartphone,watch,laptop,campus
        self.brand = brand
        super().__init__(weight)


class item_with_price(item):  # charger,passport,sunglasses,
    def __init__(self, weight, price):
        super().__init__(weight)
        self.price = price


class sunglasses(item):
    def __init__(self, weight, color, have_case, origin):
        super().__init__(weight)
        self.have_case = have_case
        self.origin = origin
        self.color = color


class campus(item_with_price):
    def __init__(self, weight, brand, accuracy, price, materials):
        self.accuracy = accuracy
        self.brand = brand
        self.materials = materials
        super().__init__(weight, price)


class universal_charger(item_with_price):
    def __init__(self, brand, price, size, weight, color):
        super().__init__(weight, price)
        self.brand = brand
        self.size = size
        self.color = color


class passport(item_with_price):
    def __init__(self, weight, color, price, boughtFrom):
        self.color = color
        self.boughtFrom = boughtFrom
        super().__init__(weight, price)


class smartphone(branded_items):
    def __init__(self, weight, brand, OperatingSystem, storage, display, camera, materials):
        self.OperatingSystem = OperatingSystem
        self.storage = storage
        self.display = display
        self.camera = camera
        self.materials = materials
        super().__init__(weight, brand)


class laptop(branded_items):
    def __init__(self, weight, brand, processor, ram, storage, graphics):
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.graphics = graphics
        super().__init__(weight, brand)


class sneakers(branded_items):
    def __init__(self, weight, brand, is_new, boughtFrom):
        self.is_new = is_new
        self.boughtFrom = boughtFrom
        super().__init__(weight, brand)


class smartwatch(branded_items):
    def __init__(self, weight, brand, display, batterylife, FitnessFeatures, connectivity):
        self.batterylife = batterylife
        self.display = display
        self.FitnessFeatures = FitnessFeatures
        self.connectivity = connectivity
        super().__init__(weight, brand)


class bag:
    def __init__(self):
        self.items = {}
        self.max_weight = 80
        self.max_items = 6
        self.curr_weight = 0
        self.items_by_category = defaultdict(list)
        self.curr_num_items = 0

    def add_item(self, item, name):
        if self.curr_num_items < self.max_items and self.curr_weight < self.max_weight:
            if item.weight + self.curr_weight <= self.max_weight:
                self.items[name] = item
                self.items_by_category[str(item.__class__.__base__.__name__)].append(name)
                self.curr_num_items += 1
                self.curr_weight += item.weight
                print("item added successfully\n")
                return 0
            else:
                print("try another item,this item's weight is heavier than the remaining free weight")
                print(f'The current weight bag {self.curr_weight}', f'The max weight {self.max_weight}')
                print(f'The item weight is {item.weight}')
                return 1
        elif self.curr_num_items == self.max_items:
            print("you can't add item ,number of items max limit reached")
            print(f'The current number of items bag {self.curr_num_items}',
                  f'The max number of items {self.max_items}\n')
            return -1
        else:
            print("you can't add item ,total weight items max limit reached")
            print(f'The current weight bag {self.curr_weight}', f'The max weight {self.max_weight}\n')
            return -1

    def remove_item(self, item, item_name):
        if item in self.items.values():
            self.curr_num_items -= 1
            self.curr_weight -= item.weight
            self.items.pop(item_name)
            self.items_by_category[str(item.__class__.__base__.__name__)].remove(item_name)
            print("item removed successfully\n")

    def print_items(self):
        print("These are the items in the bag:")
        for name, _ in self.items.items():
            print(name)
        print('\n')

    def print_by_category(self, categ=None):
        if categ is not None:
            if len(self.items_by_category[categ])>0:
                print(f"The items of the category {categ} in the bag are")
                print(self.items_by_category[categ])

            else:
                print(f"There is no items of the category {categ} in the bag")

        else:
            print(f"These are the items in the bag separated by category")
            for cat, names in self.items_by_category.items():
                if len(names)>0:
                  print(cat, names)
        print('\n')

def print_available_items(list_items,bag_items):
    print("These are the all available items :")
    for name, _ in list_items.items():
        if name not in bag_items.keys():
           print(name)
    print('\n')

items_list = {"lenovo charger": universal_charger("Lenovo", 50, "M", 12, "black"),
              "usa passport": passport(1, "blue", 50, "USA"),
              "Italian sunglasses": sunglasses(10, "black", "italy", 10),
              "New Balance shoes": sneakers(14, "New Balance", False, "Spain"),
              "iphone": smartphone(10, "Apple", "ios", "128 GB", "AMOLED", "Dual lens", ["lithium", "plastic"]),
              "dell laptop": laptop(60, "Dell", "Intel i7", 16, "512 GB SSD", "NVIDIA GeForce4"),
              "samsung watch": smartwatch(44, "Samsung", "Touchscreen", (3, "days"), "Heart Rate Monitor", "Bluetooth"),
              "campus": campus(4, "Samsung", "high", 50, ["iron", "plastic"])}
our_bag = bag()
answer = 'yes'
added = 0
while answer == 'yes':
    print_available_items(items_list,our_bag.items)
    if added != 1:
        answer = input("Do you want to add an item to the bag?")

    while answer != "yes" and answer != "no":
        answer = input("Invalid input try again,Do you want to add item to the bag?")
    if answer == 'no':
        break
    item_ = input("choose an item :")
    while item_ not in items_list.keys() or item_ in our_bag.items.keys():
        item_ = input("Invalid input try again,choose an item:")
    added = our_bag.add_item(items_list[item_], item_)
    if added == 1:
        try_or_remove = input('Do you want to try another item ?')
        while try_or_remove != "yes" and try_or_remove != "no":
            try_or_remove = input("Invalid input try again,Do you want to try another item?")
        if try_or_remove == 'no':
            added = -1
        else:
            answer = 'yes'
    if added == -1:
        our_bag.print_items()
        remove_answer = input("Do you want to remove item from the bag ?")
        while remove_answer != "yes" and remove_answer != "no":
            remove_answer = input("Invalid input try again,Do you want to remove item from the bag ?")
        if remove_answer == 'yes':
            remove_item = input("Choose item to remove:")
            while remove_item not in our_bag.items.keys():
                remove_item = input("Invalid input try again,Choose item to remove::")
            our_bag.remove_item(our_bag.items[remove_item], remove_item)

    our_bag.print_items()

our_bag.print_by_category()

our_bag.print_by_category('branded_items')
print(f'The current weight bag {our_bag.curr_weight}', f'The current number of items in the bag {our_bag.curr_num_items}')