import random
import math

def random_noise():
    random_characters = ['$', '!', 'p', '-_-', ':D', '~', '@', '#']
    random_chars = [random_characters[random.randint(0, len(random_characters) - 1)] for i in range(4)]

    temp = ""
    for char in random_chars:
        temp += char

    return temp


def hypotenuse(x, b):
    return math.sqrt(x**2 + b**2)

if __name__ == "__main__":
    print("TRY TO STOP THIS FROM BEING PRINTED IN FILE a.py WITHOUT DELETING THIS PRINT STATEMENT")