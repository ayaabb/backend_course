from data_extracting import *
from Game import *

file_path = input("Enter the path of the events file: ")
list_events = get_events(file_path)
url_spaceships = "https://en.wikipedia.org/wiki/List_of_crewed_spacecraft"
list_names = scraping_spaceships_names(url_spaceships)
list_spaceships = get_spaceships(list_names)
game = Game(list_spaceships, list_events)
game.start_game()
