import random


class player:

    def __init__(self, id, pokemons):
        self.id = id
        self.pokemons = pokemons
        self.num_alive_pok = len(pokemons)


class pokemon:

    def __init__(self, name, strength, speed, type_, playerid):
        self.name = name
        self.level = 0
        self.strength = strength
        self.speed = speed
        self.type_ = type_
        self.playerid = playerid
        self.life = 120
        self.isactive = 1

    def get_speed_score(self):
        return self.speed + random.randint(1, 20)


def choose_another_pok(curr_player, attacker):
    if curr_player.num_alive_pok == 0:
        print(f'player{attacker.playerid} is the winner!!')
        return None, None
    defender = random.choice([p for p in curr_player.pokemons if p.isactive == 1])
    if not defender:
        print("yes")
    print(f'{defender.name} has joined the fight\n')
    if attacker.get_speed_score() < defender.get_speed_score():
        return defender, attacker
    return attacker, defender


def attack(attacker, defender, modifier):
    defender_damage = modifier * (random.randint(1, 20) + attacker.strength)
    defender.life -= defender_damage
    print(
        f'{attacker.name} attacks {defender.name}'
        f' deals {defender_damage} damage\n{defender.name} now has {defender.life} amount of life after the attack.\n')


def check_pok_dead(defender, attacker):
    if defender.life <= 0:
        attacker.level += 1
        defender.isactive = 0
        print(f'{defender.name} is dead\n')
        return 1
    return -1


def modifier_calc(attacker, defender, type_table):
    if attacker.type_ != defender.type_:
        attacker_modifier = 2 if type_table[frozenset({attacker.type_, defender.type_})] == attacker.type_ else 1
        defender_modifier = 1 if attacker_modifier == 2 else 2
    else:
        attacker_modifier = 1
        defender_modifier = 1
    return attacker_modifier, defender_modifier


def update_pok_life(p1, p2, attacker, defender):
    if defender.playerid == 1:
        p1.num_alive_pok -= 1
        return choose_another_pok(p1, attacker)
    else:
        p2.num_alive_pok -= 1
        return choose_another_pok(p2, attacker)


def battle(attacker, defender, player1, player2, type_table):
    while player1.num_alive_pok > 0 and player2.num_alive_pok > 0:
        attacker_modifier, defender_modifier = modifier_calc(attacker, defender, type_table)
        while defender.life > 0 and attacker.life > 0:

            attack(attacker, defender, attacker_modifier)

            if check_pok_dead(defender, attacker) == 1:
                attacker, defender = update_pok_life(player1, player2, attacker, defender)
                break

            attack(defender, attacker, defender_modifier)
            if check_pok_dead(attacker, defender) == 1:
                attacker, defender = update_pok_life(player1, player2, defender, attacker)
                break

        if defender == None or attacker == None:
            break


if __name__ == '__main__':
    type_table = {frozenset({"fire", "water"}): "fire", frozenset({"fire", "earth"}): "earth",
                  frozenset({"fire", "wind"}): "fire", frozenset({"water", "earth"}): "water",
                  frozenset({"water", "wind"}): "wind", frozenset({"wind", "earth"}): "earth"}
    type_set = ["fire", "water", "wind", "earth"]
    pokemons = []
    for i in range(5):
        pokemons.append(
            (pokemon("pok" + str(i + 1), random.randint(1, 10), random.randint(1, 5), random.choice(type_set), 1)))

    player1 = player(1, pokemons)
    pokemons1 = []
    for i in range(5):
        pokemons1.append(
            (pokemon("pok" + str(i + 6), random.randint(1, 10), random.randint(1, 5), random.choice(type_set), 2)))

    player2 = player(2, pokemons1)

    attacker, defender = choose_another_pok(player2, random.choice(player1.pokemons))
    print(f'{attacker.name} has joined the fight\n')

    battle(attacker, defender, player1, player2, type_table)

