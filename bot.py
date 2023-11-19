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


@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    message =  """"1. Create a new spread sheet. (take care that name of spread sheet has no spaces)
2. Give editor access to given mail **autoexcelserviceaccount@autoexcel-405401.iam.gserviceaccount.com**
3. Use **/config** to setup the bot
4. Now send unsorted data to the bot and it will be sorted and added to the sheet."""
    await interaction.response.send_message(message,ephemeral=True)