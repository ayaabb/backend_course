from games import *

steam_games = games_data()
steam_url = "https://store.steampowered.com/search/hometab/TopGrossing/?time=0&hide_f2p=false"
steam_games.scraping_data_json(steam_url, 'storeitemdata', 'rgApps')
steam_games.plot_most_appeared_tags()
steam_games.print_tags()
tag = steam_games.ask_for_tag()
tag_percent = steam_games.print_percent(tag)
steam_games.plot_pie(tag, tag_percent)

