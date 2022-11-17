# bot.py
import json
import paho.mqtt.client as mqtt
import os
import discord
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = ''
intents = discord.Intents.all()

class MyClient(discord.Client):
    async def on_ready(self):
        print("Eingeloged")
    
    
    async def on_message(self, message):
        if message.author == client.user:
            return
        print(str(message.author) + str(message.content))
        insult = requests.get('https://insult.mattbas.org/api/insult.json')

        
        outFile = open("free.json", "r")
        free = json.loads(outFile.read())
        outFile.close()
        if free["free"] == 0:
            microwavetext = "!\nAnd there aren't any free microwaves, looser"
        elif free["free"] == 1:
            microwavetext = "!\nBut there is 1 free microwave, go and get it!"
        else:
            microwavetext = "!\nBut there are " + str(free["free"]) + " free microwaves, you don't even have to runn you laisy moron!"
        await message.channel.send('"' + str(message.content) + '" What should that mean?!?\n' + insult.json()["insult"] + microwavetext)
        
client = MyClient(intents=intents)
client.run(TOKEN)





