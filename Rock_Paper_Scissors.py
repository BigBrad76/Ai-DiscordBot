
import discord
from discord.ext import commands
import random

# Create a new bot instance with a specified command prefix
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

# Define a list of possible choices
choices = ["rock", "paper", "scissors"]

# Define a dictionary to determine the winner
winners = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# Define a command to play Rock-Paper-Scissors
@bot.command(name="rps", help="Play Rock-Paper-Scissors")
async def rps(ctx, user_choice: str):
    try:
        user_choice = user_choice.lower()
        if user_choice not in choices:
            await ctx.send("Invalid choice. Please choose rock, paper, or scissors.")
            return

        bot_choice = random.choice(choices)
        print(f"User choice: {user_choice}, Bot choice: {bot_choice}")

        if user_choice == bot_choice:
            await ctx.send(f"Both players selected {user_choice}. It's a tie!")
        elif winners[user_choice] == bot_choice:
            await ctx.send(f"{ctx.author.mention} wins! {user_choice.capitalize()} beats {bot_choice}.")
        else:
            await ctx.send(f"{bot_choice.capitalize()} beats {user_choice}. Better luck next time, {ctx.author.mention}!")
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred. Please try again later.")

# Event to indicate the bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

# Run the bot with your Discord bot token
bot.run("YOUR_DISCORD_BOT_TOKEN")