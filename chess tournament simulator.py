import random

import names


class player:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.total_points = 0


playres = []
for i in range(4):
    playres.append(player(names.get_full_name(), random.randint(1500, 2000)))
