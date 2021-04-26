import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('$hello'):
        await message.reply('Hello! <@' + str(message.author.id) + '>')

    if message.content.lower().startswith('$add'):
        with open('blacklist.txt', 'r') as f:
            words = f.read()
            blacklist = words.split()

        msg = message.content.lower()
        for word in blacklist:
            if word in msg:
                await message.reply(message.content[5:] + ' already exists in the blacklist <@' + str(message.author.id) + '>')
                return

        with open("blacklist.txt", "a") as writefile:
            writefile.write(' ' + message.content[5:])

        with open('blacklist.txt', 'r') as f:
            words = f.read()
            blacklist = words.split()

        await message.reply('Added <@' + str(message.author.id) + '>')
        return

    with open('blacklist.txt', 'r') as f:
        words = f.read()
        blacklist = words.split()
    
    msg = message.content.lower()

    for word in blacklist:
        if word in msg:
            await message.reply('Don\'t swear <@' + str(message.author.id) + '>')
            await message.delete()
            return
    return

key = ''

with open('key.txt','r') as f:
    key = f.read()
    
client.run(key)