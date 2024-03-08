import json
from Events import *
import requests
from bs4 import BeautifulSoup as bs
from spaceship import *


def scraping_spaceships_names(url):
    response = requests.get(url)
    data = bs(response.text, 'html.parser')
    spaceship_names = data.find(class_='vector-toc-list', id="toc-Currently_operational_crewed_spacecraft-sublist")
    spaceship_names = spaceship_names.findAll('a')
    list_names = []
    for s in spaceship_names:
        list_names.append(s.get('href').split('#')[1])
    return list_names


def get_events(file_name):
    events_file = open(file_name)
    events_file = json.load(events_file)
    list_events = []
    for event in events_file:
        list_events.append(Event(event, events_file[event]))
    return list_events


def get_spaceships(list_names):
    list_space_ships = []
    fuel = 100
    for i in range(len(list_names)):
        list_space_ships.append(spaceship(list_names[i], fuel + 20*(i+1)))
    return list_space_ships