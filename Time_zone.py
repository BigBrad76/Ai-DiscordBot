
import discord
from discord.ext import commands
import datetime
import pytz

# Create a new bot instance with a specified command prefix
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

# Define a command to display the current time in a specific timezone
@bot.command(name="time", help="Display the current time in a specific timezone")
async def time(ctx, timezone: str = "UTC"):
    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.datetime.now(tz).strftime("%H:%M:%S")
        await ctx.send(f"Current time in {timezone}: {current_time}")
    except pytz.UnknownTimeZoneError:
        await ctx.send(f"Unknown timezone: {timezone}")

# Run the bot with your Discord bot token
bot.run("YOUR_DISCORD_BOT_TOKEN")