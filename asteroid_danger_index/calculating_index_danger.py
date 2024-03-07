def calculate_danger(asteroids, A=1, B=1, C=1):  # calculating the danger index for each asteroid
    # by this equation A*(avg diameter) + B*(relative speed) * 1/C (miss distance)
    danger_index = []
    for ast in asteroids:
        avg_diameter = (ast['est_diameter_min'] + ast['est_diameter_max']) / 2
        danger_index.append(A * avg_diameter + B * ast['relative_velocity_KMH'] + C * ast['miss_distance_KM'])
    return danger_index


def ask_for_ABC_values():  # asking the user for 3 coefficients and checking if it is a natural number
    A = input("Choose 3 natural numbers to calculate the danger index :\nA=")
    while not A.isdigit():
        A = input("Invalid input,choose a number\nA= ")
    B = input('B=')
    while not B.isdigit():
        B = input("Invalid input,choose a number\nB= ")
    C = input('C=')
    while not C.isdigit():
        C = input("Invalid input,choose a number\nC= ")
    return int(A), int(B), int(C)
