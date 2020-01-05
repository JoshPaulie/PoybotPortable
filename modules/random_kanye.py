import random


def generate_inspiration():

    '''intro = None
    lines = None
    with open('resources/and_then_he.txt')as f:
        intro = f.read().splitlines()
    with open('resources/god_kanye_quotes_textfile.txt') as f:
        lines = f.read().splitlines()''' # Alt code that might work one day

    intro = open('C:\\Users\joshp\\PycharmProjects\\PoybotPortable\\resources\\and_then_he.txt').read().splitlines()
    lines = open('C:\\Users\joshp\\PycharmProjects\\PoybotPortable\\resources\\god_kanye_quotes_textfile.txt').read().splitlines()
    godsword = '> {}, "{}"'.format(random.choice(intro), random.choice(lines))
    return godsword
