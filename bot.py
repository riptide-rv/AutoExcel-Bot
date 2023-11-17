import discord
import responses


async def send_message(message):
    response = responses.handle_request(message)
    await message.channel.send(response)



def run_discord_bot():
    client.run('MTE3NDc1OTgyNTM2ODk0MDYxNg.GwcIwp.GoCPWv33agtlsiusX4LquWS8jdLpHo1TTsbIZI')


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("hi")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said:'{user_message}'")

    await send_message(message)
