import discord
from discord.ext import commands

# Create a new bot instance with a specified command prefix
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

# Define a slash command using the @bot.slash_command() decorator
@bot.slash_command(name="Helldiver", description="For Democracy!")
async def hello(ctx):
    await ctx.respond("Hello!")

# Run the bot with your Discord bot token
bot.run("YOUR_DISCORD_BOT_TOKEN")