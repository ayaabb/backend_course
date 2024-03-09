import json
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs


class games_data:
    def __init__(self):
        self.url = ''
        self.names_games_list = []
        self.tags_dict = {}
        self.tags_df = pd.DataFrame()
        self.most_appeared_tags = pd.DataFrame()
        self.sum_tags = 0

    def scraping_data_json(self, url, key1,key2):  # scraping data into json, then retrieve names and tags for each game and store the information
        self.url = url
        response = requests.get(url).json()
        data = response[key1][key2]
        df = pd.DataFrame(data)
        tags_dict = {}
        for p in df.columns:  # iterate through the tags, counting the number of games associated with each tag
            for tag in df[p]['tags']:
                if tag in tags_dict.keys():
                    tags_dict[tag] += 1
                else:
                    tags_dict[tag] = 1
        self.sum_tags = sum(tags_dict.values())
        self.tags_dict = {k: v for k, v in sorted(tags_dict.items(), key=lambda item: item[1],
                                                  reverse=True)}    # sort the tag counts and store them in a dictionary
        self.tags_df = pd.DataFrame({'Tags': list(self.tags_dict.keys()), 'Counts': list(self.tags_dict.values())})
        self.most_appeared_tags = self.tags_df[0:10]  # saving the first 10 most appeared tags in list
        with open("games_content.json", "w") as file:  # saving the data in json file
            json.dump(data, file)

    def html_data_scraping(self, url): #make a request to a specified URL, retrieving the HTML content, and then using BeautifulSoup to parse the HTML
        self.url = url
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')
        data = soup.find(class_="tab_content", id="tab_newreleases_content")
        if data is None:
            print("There is no new releases games")
            return
        self.get_names_and_tags(data)

    def get_names_and_tags(self, data):  # retrieve names and tags for each game, and store the information
        self.names_games_list = [name.text for name in data.find_all(class_='tab_item_name')]
        # iterate through the tags, counting the number of games associated with each tag
        for tag in data.find_all(class_='tab_item_content'):
            list_tags = tag.find(class_='tab_item_top_tags').find_all('span')
            for t in list_tags:
                # delete punctuation marks and redundant spaces
                t_text = t.text.split(',')
                if len(t_text) > 1:
                    t_text = t_text[1]
                else:
                    t_text = t_text[0]
                if t_text[0] == ' ':
                    t_text = t_text[1:]
                if t_text in self.tags_dict.keys():

                    self.tags_dict[t_text] += 1
                else:
                    self.tags_dict[t_text] = 1

        self.sum_tags = sum(self.tags_dict.values())
        # sort the tag counts and store them in a dictionary
        self.tags_dict = {k: v for k, v in sorted(self.tags_dict.items(), key=lambda item: item[1],
                                                  reverse=True)}
        # convert the data to data_frame to facilitate easier plotting
        self.tags_df = pd.DataFrame({'Tags': list(self.tags_dict.keys()), 'Counts': list(self.tags_dict.values())})
        # saving the first 10 most appeared tags in list
        self.most_appeared_tags = self.tags_df[0:10]

    def print_tags(self):  # display all available tags, allowing the user to choose one from the list
        print(f'These are the tags of the games : {list(self.tags_dict.keys())}')

    def ask_for_tag(self):  # asks the user to choose one of the tags and checks if it is in the tags list
        tag = input("choose a tag to show its frequency percent:")
        while tag not in self.tags_dict.keys():
            tag = input("invalid tag ,choose a tag from the list above:")
        return tag

    def plot_pie(self, tag, tag_percent):  # plot a pie chart illustrating the percentage distribution of a specific tag
        fig, ax = plt.subplots()
        ax.pie([tag_percent, 100 - tag_percent], labels=[tag, 'the rest of the tags'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
        plt.savefig(tag + '.png')

    def print_percent(self, tag):  # calculates the percent of the specific tag from the game list and prints it
        percent = format((self.tags_dict[tag] / self.sum_tags) * 100, ".2f")
        print(f'The percent of tag {tag} is {percent}%')
        return float(percent)

    def plot_most_appeared_tags(self):  # plot the most frequently appearing tags in a bar chart
        st.bar_chart(self.most_appeared_tags.set_index('Tags'))
        st.pyplot()
