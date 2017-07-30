#!/usr/bin/python3

import asyncio
import discord
import sqlite3

client = discord.Client()
db_connector = sqlite3.connect("birb.db")
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
                if user_score == None:
                    c.execute("INSERT INTO scores VALUES((?), 0)", user)
                tmp = await client.send_message(message.channel, score_user + " has gained a point")
            elif word[-2:] == "--":
                score_user = word[:-2]
                tmp = await client.send_message(message.channel, score_user + " has lost a point")
    #condition for the "fuck you"
    if msg[0] == "!":
        tmp = await client.send_message(message.channel, "Fuck you, " + msg[1:])
    if msg.startswith(key + "victory"):
        msg_short = msg.split(" ", 1)[1]

token_file = open("token.txt", "r")
token = token_file.readline().rstrip("\r\n")
token_file.close()

client.run(token)
