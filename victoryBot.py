#!/usr/bin/python3.5

import discord
import random

client = discord.Client()

victoryID = 0
serv = 0

@client.event
async def on_ready():
    channelList = client.get_all_channels()
    for c in channelList:
        if c.name == 'victories':
            global victoryID
            victoryID = str(c.id)
    for s in client.servers:
        if s.name == "birbChat":
            global serv
            serv = s
    print("Ready!")

@client.event
async def on_message(message):
    tag = '!'
    if not message.content.startswith(tag):
        return
    if message.content.startswith(tag + 'ping'):
        msg = await client.send_message(message.channel, "pong!")
    if message.content.startswith(tag + "hello"):
        msg = await client.send_message(message.channel, "Hello, " + message.author.mention)
    if message.content.startswith(tag + "victory:"):
        victory = client.get_channel(victoryID)
        mess = message.content.split(':')
        if victory == None:
            msg = await client.send_message(message.channel, "I can't access victories right now.  Try again later.")
        else:
            msg = await client.send_message(victory, message.author.mention + ", " + mess[1])
    if message.content.startswith(tag + "<3"):
        rand = random.randint(0,3)
        if rand == 0:
            msg = await client.send_message(message.channel, "Aww")
        elif rand == 1:
            msg = await client.send_message(message.channel, "I love you too, " + message.author.mention)
        elif rand == 2:
            msg = await client.send_message(message.channel, "! == not, <3 == love... do you not love me, " + message.author.mention + "?")
        elif rand == 3:
            love = serv.get_member_named("AIRHORN SOLUTIONS#6723")
            msg = await client.send_message(message.channel, "My love belongs to " + love.mention)
    if message.content.startswith(tag + "highfive"):
        mess = message.content.split(" ")
        mntn = message.mentions
        for m in mntn:
            msg = await client.send_message(m, "SMACK")
            msg2 = await client.send_message(message.channel, message.author.mention + " high-fived " + m.mention)
        msg3 = await client.send_message(message.author, "SMACK")

#def randomize():


