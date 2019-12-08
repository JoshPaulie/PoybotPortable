import random


def generateInspiration():
    lines = open('kanyeQuotes.txt').read().splitlines()
    godsword = "✝  ***Kayne West***  ✝ \n\n*" + random.choice(lines) + "*"
    return godsword
