import json
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import streamlit_folium as sf


class games_data:
    def __init__(self):
        self.url = ''
        self.tags_dict = {}
        self.tags_df = pd.DataFrame()
        self.most_appeared_tags = pd.DataFrame()
        self.sum_tags = 0

    def scraping_data_json(self, url, key1,
                           key2):  # scraping data into json,and extract the names and the tags of the games
        self.url = url
        response = requests.get(url).json()
        data = response[key1][key2]
        df = pd.DataFrame(data)
        tags_dict = {}
        for p in df.columns:  # going over the data frame columns and counting how many games have each tag
            for tag in df[p]['tags']:
                if tag in tags_dict.keys():
                    tags_dict[tag] += 1
                else:
                    tags_dict[tag] = 1
        self.sum_tags = sum(tags_dict.values())
        self.tags_dict = {k: v for k, v in sorted(tags_dict.items(), key=lambda item: item[1],
                                                  reverse=True)}  # sorting the conts of the tags and putting it in dictionary
        self.tags_df = pd.DataFrame({'Tags': list(self.tags_dict.keys()), 'Counts': list(self.tags_dict.values())})
        self.most_appeared_tags = self.tags_df[0:10]  # saving the first 10 most appeared tags in list
        with open("games_and_tags.json", "w") as file:  # saving the data in json file
            json.dump(data, file)

    # def html_data_scraping(self,url):
    #     # url = 'https://store.steampowered.com/search/?sort_by=_ASC&filter=topsellers'
    #     response = requests.get(url)
    #     soup = bs(response.text, 'html.parser')
    #
    #     game_list = soup.find_all('div', class_='responsive_search_name_combined')
    #     for game in game_list:
    #         game_name = game.find('span', class_='title')
    #         genre = game.find('span', class_='genre')
    #         print(f'Game Name: {game_name}\nGenre: {genre}\n')
    def print_tags(self):  # printing all the tags to let the user choose one of them
        print(f'These are the tags of the games : {list(self.tags_dict.keys())}')

    def ask_for_tag(self):  # asking the user to choose one of the tags and checking if it is in the tags list
        tag = input("choose a tag to show its frequency percent:")
        while tag not in self.tags_dict.keys():
            tag = input("invalid tag ,choose a tag from the list above:")
        return tag

    def plot_pie(self, tag, tag_percent):  # plot a pie plot of the percent of a specific tag
        fig, ax = plt.subplots()
        ax.pie([tag_percent, 100 - tag_percent], labels=[tag, 'the rest of the tags'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
        plt.savefig(tag + '.png')

    def print_percent(self, tag):  # calculating the percent of the specific tag from the game listan printing it
        percent = format((self.tags_dict[tag] / self.sum_tags) * 100, ".2f")
        print(f'The percent of tag {tag} is {percent}%')
        return float(percent)

    def plot_most_appeared_tags(self):  # plotting the most appeared tags in a bar chart
        st.bar_chart(self.most_appeared_tags.set_index('Tags'))
        st.pyplot()
