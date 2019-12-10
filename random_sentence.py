import random


def generate_sentence():
    adj = open('C:\\Users\\joshp\\PycharmProjects\\PoybotPortable\\adjs.txt').read().splitlines()
    noun = open('C:\\Users\\joshp\\PycharmProjects\\PoybotPortable\\nouns.txt').read().splitlines()
    names = open('C:\\Users\\joshp\\PycharmProjects\\PoybotPortable\\names.txt').read().splitlines()
    sentence = "{} is a {} {}".format(random.choice(names), random.choice(adj), random.choice(noun))
    return sentence
