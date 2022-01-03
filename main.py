import discord
import hashlib

botID = open("token.txt", "r")

TOKEN = botID.read()

client = discord.Client()


@client.event
async def on_ready():
    print("Bot turned on")


# When each message plays
@client.event
async def on_message(message):
    # ensures bot does not read itself
    if message.author == client.user:
        return
    # Takes Discord account info and message content
    username = str(message.author)
    usernameID = str(message.author.id)
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} {usernameID}: {user_message} ({channel})')
    hash_res = int(hashlib.sha256(bytes("salt " + usernameID, 'utf-8')).hexdigest(), 16)
    alignment = int(str(abs(hash_res))[0])
    if alignment == 1:
        alignment_text = "lawful good"
    elif alignment == 2:
        alignment_text = "lawful neutral"
    elif alignment == 3:
        alignment_text = "lawful evil"
    elif alignment == 4:
        alignment_text = "neutral good"
    elif alignment == 5:
        alignment_text = "true neutral"
    elif alignment == 6:
        alignment_text = "neutral evil"
    elif alignment == 7:
        alignment_text = "chaotic good"
    elif alignment == 8:
        alignment_text = "chaotic neutral"
    elif alignment == 9:
        alignment_text = "chaotic evil"
    else:
        alignment_text = "true neutral"
    await message.channel.send(f"You are {alignment_text}.")


botID.close()

client.run(TOKEN)
