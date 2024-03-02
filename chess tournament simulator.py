import random

import names


class player:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.total_points = 0


players = []
for i in range(4):
    players.append(player(names.get_full_name(), random.randint(1500, 2000)))

players_per_round = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]

c = 0
for j in range(3):
    print(f"Round {j + 1} :")
    for i in range(2):
        reversed_ratio = 1 - (
                    players[players_per_round[c + i][0]].ranking / players[players_per_round[c + i][1]].ranking)
        print(
            f"Player {players[players_per_round[c + i][0]].name} vs Player {players[players_per_round[c + i][1]].name}\n"
            f"player {players_per_round[c + i][0] + 1} ranking is {players[players_per_round[c + i][0]].ranking} \n"
            f"player {players_per_round[c + i][1] + 1} ranking is {players[players_per_round[c + i][1]].ranking}\n"
            f"the ratio = {1 - reversed_ratio}\n"
            f"reversed ratio= {reversed_ratio}\n"
            f"player {players_per_round[c + i][0] + 1} chances of winning = {0.4 - reversed_ratio}\n"
            f"player {players_per_round[c + i][1] + 1} chances of winning = {0.4 + reversed_ratio}\n")
        if reversed_ratio == 0:
            print("Draw!!")
            players[players_per_round[c + i][0]].total_points += 0.5
            players[players_per_round[c + i][1]].total_points += 0.5
        elif reversed_ratio > 0:
            print(f"The winner of this round is player {players_per_round[c + i][1] + 1}")
            players[players_per_round[c + i][1]].total_points += 1
        else:
            print(f"The winner of this round is player {players_per_round[c + i][0] + 1}")
            players[players_per_round[c + i][0]].total_points += 1
        print("\n")
    c += 2
max_points=0
winner_player=""
for p in players:
    if p.total_points>max_points:
        max_points=p.total_points
        winner_player=p.name
print(f"The winner of this tournament is {winner_player} with total points {max_points}")