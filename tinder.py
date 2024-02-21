import copy
class User:
    def __init__(self, name, gender, age, profession, tv_show, favorite_food):
        self.name = name
        self.gender = gender
        self.age = age
        self.profession = profession
        self.tv_show = tv_show
        self.favorite_food = favorite_food


if __name__ == '__main__':
    names = ["Sara", "David", "Sam", "Lora"]
    genders = [2, 1, 2, 1]  # 1 Male , 2 Female
    ages = [25, 30, 23, 40]
    professions = ["coach", "engineer", "chef", "teacher"]
    serieses = ["friends", "prison break", "planet", "blacklist"]
    foods = ["burger", "soup", "meat", "pizza"]
    users = []

    for i in range(4):
        users.append(User(names[i], genders[i], ages[i], professions[i], serieses[i], foods[i]))
    while 1:
        name = input(f'enter your name: ')
        gender = int(input(f'enter your gender(1 for Male,2 for Female): '))
        while gender != 1 and gender != 2:
            gender = int(input(f'Invalid input ,enter your gender again(1 for Male,2 for Female): '))
        age = int(input(f'enter your age ,it has to be between {min(ages)} and {max(ages)}: '))
        while age > max(ages) or age < min(ages):
            age = int(input(f'Invalid input, enter your age again,it has to be between {min(ages)} and {max(ages)}: '))

        profession = input(f'enter your profession: ')
        series = input(f'enter your series: ')
        food = input(f'enter your favorite food ,it has to be {foods}: ')
        while food not in foods:
            food = input(f'Invalid input,enter your favorite food again,it has to be {foods}: ')
        for u in users:
            if gender != u.gender:
                if u.age > age and gender == 2:
                    print(f'your profile matches with {u.__dict__} ')
                    exit()
                elif age > u.age and gender == 1:
                    print(f'your profile matches with {u.__dict__} ')
                    exit()

        print(f'your profile does not match any user ,try again')