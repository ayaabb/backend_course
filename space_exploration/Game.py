class Game:
    def __init__(self, spaceships, events):
        self.spaceships = spaceships
        self.events = events
        self.coins = 0

    def ask_for_space_ships(self):
        for i in range(len(self.spaceships)):
            print(f'{i + 1}_ {self.spaceships[i]}')
        ship = int(input(f'Choose a spaceship to start the game: '))
        while ship > len(self.spaceships) or ship < 1:
            ship = int(input(f'Invalid input ,Choose a spaceship from above: '))
        return self.spaceships[ship - 1]

    def start_game(self):
        player_ship = self.ask_for_space_ships()
        player_ship.launch_spaceship()
        while player_ship.health > 0 and player_ship.fuel > 0:

            player_ship.explore_galaxy(self.events)
            player_ship.update_fuel()
            print(player_ship)
            if player_ship.health <= 0:
                print(f"{player_ship.name} has been destroyed. Game over!")
                break
            if player_ship.fuel <= 0:
                print(f"{player_ship.name} has run out of fuel. Game over!")
                break
            want_exploring = input("Do you want to continue exploring? (yes/no) ").lower()
            if want_exploring != 'yes':
                print(f"{player_ship.name} returns from the space exploration. Game over!")
                break
