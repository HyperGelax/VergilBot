import discord
from discord.ext import commands
import json

intents = discord.Intents.default()

client = commands.Bot(command_prefix='?', intents=intents)

TOKEN = 'оно ругается когда я кидаю токен'

try:
    with open('sent_messages.json', 'r') as f:
        sent_messages = json.loads(f.read())
except FileNotFoundError:
    sent_messages = {}

with open('sent_messages.json', 'w') as f:
    f.write(json.dumps(sent_messages))


@client.event
async def on_ready():
    print(f'{client.user.name} успешно подключился к Discord серверу!')
    for guild in client.guilds:
        channel = discord.utils.get(guild.channels, name='основной')
        if channel and str(guild.id) in sent_messages:
            message = f"Я был успешно перерожден и готов к работе на сервере {guild.name}."
            sent_messages[str(guild.id)] = message
            await channel.send(message)

        elif channel:
            await channel.send(f'`Покажи мне свою мотивацию! \n'
                               f' "?help" для вызова помощи`')

        with open('sent_messages.json', 'w') as f:
            f.write(json.dumps(sent_messages))


client.run(TOKEN)
