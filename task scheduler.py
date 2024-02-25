class task:
    def __init__(self, name, duration, day=None, starting_hour=None):
        self.name = name
        self.duration = duration
        self.day = day
        self.starting_hour = starting_hour


def ask_for_task():
    more_task = input("Do you have more tasks?")
    while more_task != "yes" and more_task != "no":
        more_task = input("Invalid input try again,do you have more tasks?")
    if more_task == "yes":
        task_name = input("Enter the name of the task: ")
        task_duration = input("Enter the duration of the task: ")
        while not task_duration.isdigit() or int(task_duration) > 8:
            task_duration = input("Invalid input try again,enter the duration of the task: ")
        answer = input("Do task have a specific day and starting hour? ")
        while answer != 'no' and answer != 'yes':
            answer = input("Invalid input try again,do task have a specific day and starting hour? ")
        if answer == 'no':
            return task(task_name, int(task_duration))
        elif answer == 'yes':
            day, start_hour = input("Enter a specific day and a starting hour : ").split()
            while not day.isdigit() or not start_hour.isdigit() or int(task_duration) + int(start_hour) > 9 or int(
                    day) > 5:
                day, start_hour = input("Invalid input try again,enter a specific day and a starting hour : ").split()
            return task(task_name, int(task_duration), int(day), int(start_hour))

    return None


def find_free_time(task, days):
    for j in range(len(days)):
        c = 0
        for i in range(len(days[j]) - 1):
            if task.duration == 1:
                if days[j][i] is None:
                    return j + 1, i + 1
                if i == len(days[j]) - 2 and days[j][i + 1] is None:
                    return j + 1, i + 2
            if days[j][i] is None and days[j][i + 1] is None:
                c += 1
                if c == task.duration - 1:
                    return j + 1, c - i if c > i else i - c + 2
            else:
                c = 0

    return -1, -1


def populate(task, free_day, free_hour, days):
    if task.day is None:
        task.day = free_day
        task.starting_hour = free_hour
    for i in range(task.duration):
        days[free_day - 1][free_hour + i - 1] = task
    task.duration = 0


def overwrite_task(new_task, days):
    old_tasks = []
    for i in range(new_task.duration):
        old_task = days[new_task.day - 1][new_task.starting_hour + i - 1]
        if old_task is not None:
            old_tasks.append(old_task)
            old_task.duration += 1
            days[new_task.day - 1][new_task.starting_hour + i - 1] = None
    populate(new_task, new_task.day, new_task.starting_hour, days)
    for t in old_tasks:
        d, h = find_free_time(t, days)
        if d != -1 and h != -1:
            populate(t, d, h, days)


def check_not_populated(task, days):
    for i in range(task.duration):
        if task.starting_hour - 1 + i < 8:
            task_ = days[task.day - 1][task.starting_hour - 1 + i]
            if task_ is not None:
                return 1
    return 0


def task_scheduler():
    days = [[None for _ in range(8)] for _ in range(5)]

    task = ask_for_task()
    while task:
        if task.day is not None and task.starting_hour is not None:
            populated = check_not_populated(task, days)

            if populated:
                overwrite = (input("Do you want to overwrite the old task with the new task ?"))
                while overwrite != "yes" and overwrite != "no":
                    overwrite = input(
                        "Invalid input try again, Do you want to overwrite the old task with the new task ?")
                if overwrite == 'yes':
                    print("ok we will overwrite old task")
                    overwrite_task(task, days)
                else:
                    print("ok we will find another spot")
                    free_day, free_hour = find_free_time(task, days)
                    print(free_day, free_hour)
                    if free_day != -1 and free_hour != -1:
                        populate(task, free_day, free_hour, days)
                    else:
                        print("there is no spot for this task!! ,try another")

            else:
                populate(task, task.day, task.starting_hour, days)
        else:
            free_day, free_hour = find_free_time(task, days)
            if free_day != -1 and free_hour != -1:
                populate(task, free_day, free_hour, days)
            else:
                print("there is no spot for this task!! ,try another")

        task = ask_for_task()
    print_schedule(days)


def print_schedule(days):
    print(f"hours :          ", end=" ")
    for x in range(1, 9):
        print(x, end="   ")
    print("\n")
    for j in range(len(days)):
        print(f'Day number {j + 1} :  ', end=" ")
        for i in range(len(days[j])):
            if days[j][i]:
                print(f'{days[j][i].name}', end='  ')
            else:
                print(" -- ", end="")
        print("\n")


task_scheduler()
