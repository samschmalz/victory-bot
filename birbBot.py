#!/usr/bin/python3

import asyncio
import discord
import sqlite3

client = discord.Client()

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
                tmp = await client.send_message(message.channel, word[:-2] + " has gained a point")
            elif word[-2:] == "--":
                tmp = await client.send_message(message.channel, word[:-2] + " has lost a point")
    #condition for the "fuck you"
    if msg[0] == "!":
        tmp = await client.send_message(message.channel, "Fuck you, " + msg[1:])
    if msg.startswith(key + "victory"):
        msg_short = msg.split(" ", 1)[1]

token_file = open("token.txt", "r")
token = token_file.readline().rstrip("\r\n")
token_file.close()

client.run(token)
