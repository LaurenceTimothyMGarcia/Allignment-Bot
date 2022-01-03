import discord
import random

botID = open("token.txt", "r")

TOKEN = botID.read()

client = discord.Client()

@client.event
async def on_ready():
   print("Bot turned on")



botID.close()

client.run(TOKEN)