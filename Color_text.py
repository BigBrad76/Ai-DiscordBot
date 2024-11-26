import discord
from discord.ext import commands

# Create a new bot instance with a specified command prefix
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

# Define a command to change the text color
@bot.command(name="color", help="Change the text color")
async def color(ctx, color: str):
    colors = {
        "red": 0xFF0000,
        "green": 0x00FF00,
        "blue": 0x0000FF,
        "yellow": 0xFFFF00,
        "purple": 0xFF00FF,
    }

    if color.lower() in colors:
        embed = discord.Embed(description="This is a colored embed!", color=colors[color.lower()])
        await ctx.send(embed=embed)
    else:
        await ctx.send("Invalid color. Available colors: red, green, blue, yellow, purple.")

# Run the bot with your Discord bot token
bot.run("YOUR_DISCORD_BOT_TOKEN")