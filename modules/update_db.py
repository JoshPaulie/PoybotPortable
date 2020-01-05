from riotwatcher import RiotWatcher
from prettytable import PrettyTable
import pandas as pd
import openpyxl as pyxl
from modules.league_key import get_league_key

watcher = RiotWatcher(get_league_key())

# Summoner Names as list
summonerNames = ['joshpaulie', 'mltsimpleton', 'poydok', 'boxrog', 'artificialmeat', 'roninalex', 'cradmajone',
                 'grillmasterlou', 'darthmrow', 'atoxichobo', 'ectoplax', 'vynle']
list.sort(summonerNames)  # This function Sorts summoner names alphabetically

# Region Set
my_region = 'na1'


def update_GRD():
    for players in summonerNames:
        me = watcher.summoner.by_name(my_region, players)
        my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])

        for rank in my_ranked_stats:
            if 'RANKED_SOLO_5x5' == rank['queueType']:
                my_solo_stats = rank

        total_solo_wins = my_solo_stats['wins']
        total_solo_losses = my_solo_stats['losses']
        solo_win_rate = round((total_solo_wins / (total_solo_losses + total_solo_wins) * 100))
        solo_tier = my_solo_stats['tier']
        solo_rank = my_solo_stats['rank']
        solo_lp = my_solo_stats['leaguePoints']
        goonSummoner = my_solo_stats['summonerName']

        goonTable.add_row([players, solo_tier + " " + solo_rank, solo_lp, solo_win_rate])
    return "```" + str(goonTable) + '```'

