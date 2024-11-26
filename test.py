import discord #The nice discord library. 
import os #To run discord on this computer.
from dotenv import load_dotenv #This is how we load our Token from a different file to keep it secure. 
from typing import Final #This is something that allows us to make our Token unchangable in the code. 

#This is token loading code
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

#Bot setup code.
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#Message functionality code, the purpose of it is to allow the bot to see messages and respond to them. It has a feature in it that allows it to DM a user instead of respond in a server channel. 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("-help"):
        await message.channel.send("Hey! Right now I don't have any options, but my developers will be making some.")
    elif message.content.startswith("-hello"):
        await message.channel.send(f"Hiya, {message.author} how can I help you today!")
    elif message.content.startswith("-give me help options"):
        await message.channel.send(f"Hello, {message.author}, here are the options we have avalible. 1 2 3")
    elif message.content.startswith("-1"):
        await message.channel.send("God will bless the USA")
    elif message.content.startswith("lol"):    
        await message.channel.send("Hahahaha you are so funny my guy")
    elif message.content.startswith("epix"):
        await message.channel.send("Do you mean Epic? jk")  
    elif message.content.startswith("lets goo"):
        await message.channel.send("lets gooooooo!🔥🙌🙌")
    elif message.content.startswith("how is my mom?"):
        await message.channel.send("she is doing good she was with me last night")
    elif message.content.startswith("when is my birthday"):
        await message.channel.send("Idk you tell me!😂🤣😂🤣")

#Bot startup code. 
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")

#This is where we bring the token to talk to Discord.
def main() -> None:
    client.run(token=TOKEN)

#This is somehow dangerously important and if you delete it the code doesn't work but idk why. 
if __name__ == "__main__":
    main()






