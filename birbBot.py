#!/usr/bin/python3

import asyncio
import discord
import sqlite3
from diceRolls import *

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
        roll_split = msg.strip().split(" ", 1)
        if len(roll_split) != 2:
            await client.send_message(message.channel, "usage: /roll [-ad] *x*d*y* [+ modifiers] [+*w*d*z* [+ modifiers]] [#comment]")
        else:
            roll_split = roll_split[1]
            if "-a" in roll_split:
                advantage = roll_split.split("-a")[1]
                dice, mods, comm = parseRolls(advantage)
                roll_test = diceRoll(dice)
                roll = max(diceRoll(dice)[0], diceRoll(dice)[0])
                print_string = rollString([roll], mods, comm)
                await client.send_message(message.channel, message.author.mention + "'s roll w/ advantage: " + print_string)
            elif "-d" in roll_split:
                disadvantage = roll_split.split("-d", 1)[1]
                dice, mods, comm = parseRolls(disadvantage)
                roll = min(diceRoll(dice)[0], diceRoll(dice)[0])
                print_string = rollString([roll], mods, comm) #roll is in brackets to force it to act like an array of 1 item
                await client.send_message(message.channel, message.author.mention + "'s roll w/ disadvantage: " + print_string)
            else:
                dice, mods, comm = parseRolls(roll_split)
                rolls = diceRoll(dice)
                print_string = rollString(rolls, mods, comm)
                await client.send_message(message.channel, message.author.mention + "'s rolls: " + print_string)

token_file = open("token.txt", "r")
token = token_file.readline().rstrip("\r\n")
token_file.close()

db_connector.close()
client.run(token)
