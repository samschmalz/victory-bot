#!/usr/bin/python3

import random

#diceroll
#returns an array of dice roll values
#roll_params: a list of roll parameters in the form xdy
def diceRoll(roll_params):
    roll_array = []
    for r in roll_params:
        num, die = r.strip().split('d')
        num = int(num)
        for n in range(num):
            roll_array.append(random.randint(1,int(die)))
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
            mod_array.append(int(item))
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

def rollString(rolls, mods, comm):
    result = str(rolls[0])
    for r in rolls[1:]:
        result += " + " + str(r)
    for m in mods:
        result += " + " + str(m)
    result += " = " + str(sum(rolls) + sum(mods))
    if len(comm) != 0:
        result += " #" + comm
    return result
