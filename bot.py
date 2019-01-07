import discord
from discord.ext import commands
import os
from discord.ext import commands
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = ['Youtube Music Dinliyor.', 'Oyun Oynuyor.', 'Korku Film izliyor.']

players = {}

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
	
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(20)

@client.event
async def on_ready():
    print('Bot ONLINE.')

@client.command(pass_context=True)
async def katıl(ctx):
   channel = ctx.message.author.voice.voice_channel
   await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def cık(ctx):
   server = ctx.message.server
   voice_client = client.voice_client_in(server)
   await voice_client.disconnect()

@client.command(pass_context=True)
async def baslat(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def dur(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def durdur(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def devam(ctx):
    id = ctx.message.server.id
    players[id].resume()

client.loop.create_task(change_status())

	
client.run(os.environ.get('token'))
