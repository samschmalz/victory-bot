#!/usr/bin/python3

import asyncio
import discord
import sqlite3
import random

client = discord.Client()
db_connector = sqlite3.connect("birb_db.sqlite")
c = db_connector.cursor()

key = "~"

@client.event
async def on_ready():
    for c in client.get_all_channels():
        if c.name == "victories":
            global victory_chan
            victory_chan = str(c.id)
    for s in client.servers:
        if s.name == "birbChat":
            global birbs
            birbs = s
    print("Bot is ready!")

@client.event
async def on_message(message):
    msg = message.content
    if msg[0] != "~":
        msg_broken = msg.split(" ")
        for word in msg_broken:
            if word[-2:] == "++":
                score_user = word[:-2]
                user = (score_user,)
                c.execute("SELECT * FROM scores WHERE player=?", user)
                user_score = c.fetchone()
                score_val = 0
                if user_score == None:
                    c.execute("INSERT INTO scores VALUES((?), 0)", user)
                    db_connector.commit()
                else:
                    score_val = user_score[1]
                score_val += 1
                score_tuple = score_val, score_user
                c.execute("UPDATE scores SET score=? WHERE player=?", score_tuple)
                db_connector.commit()
                tmp = await client.send_message(message.channel, score_user + " has gained a point for " + str(score_val) + " points")
            elif word[-2:] == "--":
                score_user = word[:-2]
                user = (score_user,)
                c.execute("SELECT * FROM scores WHERE player=?", user)
                user_score = c.fetchone()
                score_val = 0
                if user_score == None:
                    c.execute("INSERT INTO scores VALUES((?), 0)", user)
                    db_connector.commit()
                else:
                    score_val = user_score[1]
                score_val -= 1
                score_tuple = score_val, score_user
                c.execute("UPDATE scores SET score=? WHERE player=?", score_tuple)
                db_connector.commit()
                tmp = await client.send_message(message.channel, score_user + " has lost a point for " + str(score_val) + " points")
    #condition for the "fuck you"
    if msg[0] == "!":
        tmp = await client.send_message(message.channel, "Fuck you, " + msg[1:])
    if msg.startswith(key + "victory"):
        msg_short = msg.split(" ", 1)[1]
    if msg.startswith("/roll"):
        roll_split = msg.split(" ", 1)
        if len(roll_split) != 2:
            await client.send_message(message.channel, "usage: /r *x*d*y* [+ modifiers] [+*w*d*z* [+ modifiers]] [-ad] [#comment]")
        else:
            roll_split = roll_split[1]
            if "-a" in roll_split:
                advantage = roll_split.split("-a")
                advantage = [item.strip() for item in advantage]
                roll_list = advantage[0].split('+')
                first_roll = diceroll(roll_list)
                second_roll = diceroll(roll_list)
                if sum(first_roll) > sum(second_roll):
                    await client.send_message(message.channel, '@' + str(message.author) + " 's rolls: " + print_rolls(first_roll))
                elif sum(first_roll) < sum(second_roll):
                    await client.send_message(message.channel, '@' + str(message.author) + " 's rolls: " + print_rolls(second_roll))
                else:
                    if 20 in second_roll:
                        await client.send_message(message.channel, '@' + str(message.author) + " 's rolls: " + print_rolls(second_roll))
                    else:
                        await client.send_message(message.channel, '@' + str(message.author) + " 's rolls: " + print_rolls(first_roll))
            elif "-d" in roll_split:
                print("-d")
            else:
                comment_split = roll_split.split("#")
                roll_list = comment_split[0].split('+')
                roll_string = print_rolls(diceroll(roll_list))
                if len(comment_split) == 2:
                    roll_string += " " + comment_split[1]
                await client.send_message(message.channel, message.author.mention + "'s rolls: " + roll_string)

token_file = open("token.txt", "r")
token = token_file.readline().rstrip("\r\n")
token_file.close()

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

def print_rolls(roll_list):
    output = ""
    for item in roll_list[:-1]:
        output += str(item) + " + "
    output += str(roll_list[-1]) + " = " + str(sum(roll_list))
    return output

db_connector.close()
client.run(token)
