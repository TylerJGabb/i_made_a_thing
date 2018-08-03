from os import system, name
from time import sleep
import string
import random
collection = [x for x in string.ascii_letters + ' ,!']
random.shuffle(collection)

def write(s):
    print(s, end='', flush=True)
    

def clear():
    system('clear')

def get_letter():
    return random.choice(collection)

def main():
    phrase = 'Hello World!'
    generated = ''
    pos = 0
    while(generated != phrase):
        clear()
        letter = get_letter()
        temp = generated + letter
        write(temp)
        if letter == phrase[pos]:
            generated += letter
            pos += 1


main()

