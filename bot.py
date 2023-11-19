import discord
import responses
import configmodal

from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def send_message(message):
    response = responses.handle_request(message)
    await message.channel.send(response)



def run_discord_bot():
    bot.run('MTE3NDc1OTgyNTM2ODk0MDYxNg.G9mB8L.fRczfvYs6nU1l7-RHVJxLybvZ2dnhqlYyx6dag')


client = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("hi")
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said:'{user_message}'")
    async with message.channel.typing():
        await send_message(message)


@bot.tree.command(name="config")
async def config(interaction: discord.Interaction):
    await interaction.response.send_modal(configmodal.ConfigModal(title="Config"))
