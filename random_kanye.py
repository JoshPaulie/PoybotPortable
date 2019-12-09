import random


def generate_inspiration():
    lines = open('god_kanye_quotes_textfile.txt').read().splitlines()
    godsword = "✝  ***Kayne West***  ✝ \n\n*" + random.choice(lines) + "*"
    return godsword
