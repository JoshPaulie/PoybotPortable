import random


def generate_emoji():
    emojilist = '😊','😘','👌','😘','💕','🤖','✌','😜','😎','😆','😃','🤩','😎','😛'
    return random.choice(emojilist)

# open('C:\\Users\\joshp\\PycharmProjects\\PoybotPortable\\resources\\listofemojis.txt').read().splitlines()