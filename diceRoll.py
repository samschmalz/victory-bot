#!/usr/bin/python3

import random

#diceroll
#returns an array of dice roll values
#roll_params: a list of roll parameters in the form xdy
def diceroll(roll_params):
    roll_array = []
    for r in roll_array:
        num, die = r.strip().split('d')
        roll_array.append(random.randint(1,die))
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

    return roll_array, mod_array, comment

def checkRoll(param):
    if 'd' not in param:
        return False
    front, back = param.split('d',1)
    if not front.isdigit() or not back.isdigit():
        return False

    return True
