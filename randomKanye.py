import random


def generate_inspiration():
    lines = open('kanyeQuotes.txt').read().splitlines()
    godsword = "✝  ***Kayne West***  ✝ \n\n*" + random.choice(lines) + "*"
    return godsword
