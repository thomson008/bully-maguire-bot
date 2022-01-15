import os
import discord
import random
from keep_alive import keep_alive
from sentiment import is_negative
from sentiment import translator

client = discord.Client()

# Basic encouraging messages that the bot will send
tobey_quotes = [
    "I'm gonna put some dirt in your eye!",
    "Gonna cry?",
    "You want forgiveness? Get religion.",
    "You'll get you your rent when you fix this damn door!",
    "That's a cute outfit! Did your husband give it to you?",
    "See ya, chump!",
    "You're trash!",
    "Stings, doesn't it?",
    "I missed the part where that's my problem."
]

spider_words = ['spider', 'tobey', 'maguire', 'spidey', 'bully']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    """
    Handles any incoming message
    """
    if message.author == client.user or message.author.bot:
        return

    msg = message.content
    lang, negative = is_negative(msg)

    if negative:
        response = random.choice(tobey_quotes)
        if lang != 'en':
            response = translator.translate(response, dest=lang).text
        await message.channel.send(response)
    if any(word in msg.lower() for word in spider_words):
        await message.channel.send('<:tobey:930462181294764112>')


keep_alive()
client.run(os.environ['TOKEN'])