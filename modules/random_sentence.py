import random


def generate_sentence(arg):
    adj = open('C:\\Users\\joshp\\PycharmProjects\\PoybotPortable\\resources\\adjs.txt').read().splitlines()
    noun = open('C:\\Users\\joshp\\PycharmProjects\\PoybotPortable\\resources\\nouns.txt').read().splitlines()
    sentence = "{} is a {} {}".format(arg, random.choice(adj), random.choice(noun))
    return sentence
