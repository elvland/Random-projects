
import discord
import os
from datetime import datetime


from discordAPI import get_nextMatch_info

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)
#Token()



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$Hello"):
        await message.channel.send("Hello Olle, Vad vill du ha hjälp med?")

    if message.content.startswith("Barca"):
        channel = message.channel
        await send_match_info(channel)

@client.event
async def on_ready():  # Use on_ready event instead of onConnect
    print("Bot connected to the server!")
    channel = client.get_channel(1217883574993158164)
    await channel.send("Botten är redo")
    await send_match_info(channel)

async def send_match_info(channel):
    gameType, matchNum, homeTeam, awayTeam, gameDate, compType, homeBadge, awayBadge = get_nextMatch_info()
    timeUntil = calculate_time_difference(gameDate)

    # Format the time until the match
    days, seconds = timeUntil.days, timeUntil.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    time_until_str = f"{days} days, {hours} hours, {minutes} minutes"

    # Create Discord message with embedded images
    embed = discord.Embed(title="Barcelona Match Info", color=0x00ff00)
    embed.add_field(name="Match", value=f"{homeTeam} - {awayTeam} , {gameDate} ", inline=False)
    embed.add_field(name="Match Type", value=f"Game Type: {gameType}\nMatchday: {matchNum}/38", inline=False)
    embed.add_field(name="Teams", value=f"Home Team: {homeTeam}\nAway Team: {awayTeam}", inline=False)
    embed.add_field(name="Date", value=f"{gameDate}\nTime Until gameday: {time_until_str}", inline=False)
    embed.add_field(name="Stage", value=f"{compType} match", inline=False)

    # Send the info regarding the API to the Discord server
    await channel.send("@everyone !!! :soccer: :soccer:  :soccer:  :soccer:  :soccer: :soccer:\n")
    await channel.send(embed=embed)
    await channel.send("https://www.fcbarcelona.com/en/football/first-team/schedule")
    await channel.send(":soccer: :soccer:  :soccer:  :soccer:  :soccer: :soccer:\n")

def calculate_time_difference(game_date_str):
    # Convert game date string to datetime object
    game_date = datetime.strptime(game_date_str, "%Y-%m-%dT%H:%M:%SZ")

    # Get current date and time
    current_date = datetime.utcnow()

    # Calculate time difference
    time_difference = game_date - current_date

    return time_difference



client.run(TOKEN)
