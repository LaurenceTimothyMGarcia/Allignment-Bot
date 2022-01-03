import discord
import random

botID = open("token.txt", "r")

TOKEN = botID.read()

client = discord.Client()

#On start up
@client.event
async def on_ready():
   print("Bot turned on")

#When each message plays
@client.event
async def on_message(message):
   #ensures bot does not read itself
   if message.author == client.user:
      return

   #Takes Discord account info and message content
   username = str(message.author)
   usernameID = str(message.author.id)
   user_message = str(message.content)
   channel = str(message.channel.name)
   print(f'{username} {usernameID}: {user_message} ({channel})')

   

botID.close()

client.run(TOKEN)