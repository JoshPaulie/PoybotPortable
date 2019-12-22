import random


def generate_inspiration():
    intro = open('C:\\Users\joshp\\PycharmProjects\\PoybotPortable\\resources\\and_then_he.txt').read().splitlines()
    lines = open('C:\\Users\joshp\\PycharmProjects\\PoybotPortable\\resources\\god_kanye_quotes_textfile.txt').read().splitlines()
    godsword = '{}, "{}"'.format(random.choice(intro), random.choice(lines))
    return godsword


