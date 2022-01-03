import discord
import hashlib
import json

#format for dictionary works as the following: word: (chaotic-lawful) (evil-good)

botID = open("token.txt", "r")

TOKEN = botID.read()
with open('allignDict.json', 'r') as f:
    align = json.load(f)

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
    if message.content.lower().startswith("!alignment"):
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
    elif message.content.lower().startswith("!history"):
        await message.channel.trigger_typing()
        messages = []
        async for my_message in message.channel.history(limit=None).filter(
                lambda x:
                x.author.id == message.author.id and not x.content.lower().startswith("!alignment")
                and not x.content.lower().startswith("!history")
        ):
            messages.append(my_message)
            if len(messages) > 100:
                break
        # print([msg.content for msg in messages])
        # print(len(messages))
        await message.channel.send(len(messages))


botID.close()

client.run(TOKEN)
