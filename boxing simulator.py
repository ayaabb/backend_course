import random


def fight(moves, fight_type, num_rounds):
    curr_round = 1
    user_points = 0
    opp_points = 0
    print(f'{fight_type} fight is starting and the number of the rounds is {num_rounds}')
    while num_rounds >= curr_round:
        user_move = input(
            f"Round number {curr_round}\nEnter your boxing move by it's number: \n1->Jab\n2->Cross\n3->Hook\n4->Uppercut\n")
        while not user_move.isdigit() or int(user_move) > 4 or int(user_move) < 1:
            user_move = (input("Invalid input,please try again \n1->Jab\n2->Cross\n3->Hook\n4->Uppercut\n"))
        user_move = int(user_move)
        opponent_move = random.randint(1, 4)
        print(f"Your opponent move is {opponent_move}")
        if opponent_move in moves[user_move]:
            print("You won this round")
            user_points += 1
            curr_round += 1
        elif user_move in moves[opponent_move]:
            print("You lost this round")
            opp_points += 1
            curr_round += 1
        elif user_move == opponent_move:
            print("Draw!!")
            curr_round += 1
        print(f'until now your total points is {user_points} , your opponent total points is {opp_points}\n ')
        if curr_round > num_rounds and opp_points == user_points:
            print("Draw!! let's try one more round")
            num_rounds += 1

    if opp_points > user_points:
        print(f"You lost {fight_type} fight , your opponent won")
    else:
        print(f"Congratulations you won {fight_type} fight!!!! ")


if __name__ == '__main__':
    moves = {1: [2, 4], 2: [3], 3: [1, 4], 4: [2]}   # key --> winning move  , value --> losing moves to the key move
    num_rounds = {"Championship": 6, "Regular": 3}
    fight_type = input("Choose which type of fight you want ?\n1->regular\n2->championship\n")
    while not fight_type.isdigit() or (int(fight_type) != 1 and int(fight_type) != 2):
        fight_type = input("Invalid input,please try again \n1->regular\n2->championship\n")

    fight_type = "Championship" if int(fight_type) == 2 else "Regular"
    fight(moves, fight_type, num_rounds[fight_type])
