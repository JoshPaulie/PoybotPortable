import random
from pathlib import Path


base_path = Path('C:\\Users\joshp\\PycharmProjects\\PoybotPortable\\resources')

games_list = open(base_path / 'games.txt').readlines()

def generate_random_game():
    ran_game = random.choice(games_list)
    return ran_game