# Discord DND Alignment Bot

A Python based Discord bot constructed by Sebastian Clancy and Laurence Timothy Garcia.

This bot looks through a user's message history in the Discord messaging app and gives out a rating based on the Dungeon and Dragons morality system.

The rating is based on words placed in a dictionary that has been created by us. We will be providing a sample dictionary in sampleDict.json.

Each word is a key and is provided 2 values. The first value determines the user's ethics and respect towards rules, which covers Chaotic, Neutral, and Lawful. The second value determines their morals, such as kindness and harshness, which covers Evil, Neutral, and Good.

The values will be added together and divided by the amount of words added and will provide a final rating that will be given back to the user.
