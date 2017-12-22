#!/usr/bin/python3

import random

#diceroll
#returns an array of dice roll values
#roll_params: a list of roll parameters in the form xdy
def diceroll(roll_params):
    roll_array = []
    for param in roll_params:
        if 'd' in param:
            p = param.split("d")
            dice_count = int(p[0].strip())
            dice_value = int(p[1].strip())
            for roll in range(dice_count):
                roll_array.append(random.randint(1, dice_value))
        else:
            roll_array.append(int(param.strip()))
    return roll_array

#parseRolls
#roll_string: the string containing roll info
#returns: a tuple of arrays, one with rolls and one with mods
def parseRolls(roll_string):
    roll_array = []
    mod_array = []
    comment = ""
    if '#' in roll_string:
        roll_string, comment = roll_string.strip().split('#')
    for item in roll_string.strip().split():
        if 'd' in item and checkRoll(item):
            roll_array.append(item)
        elif item.isnumeric():
            mod_array.add(item)
        else:
            continue

    return tuple(roll_array, mod_array, comment)

def checkRoll(param):
    return True
