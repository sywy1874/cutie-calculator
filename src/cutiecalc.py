#Imports
#======================================================================================================================
import os
import discord
import random as rnd
from discord.ext import commands
from dotenv import load_dotenv
#======================================================================================================================

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix="??")

@bot.event
async def on_ready():
    print("Bot Is Ready And Online!")

#Decorator to specify that the method is a command
@bot.command(name='howcuteis')
async def howcuteis(ctx, usr: discord.Member):
    phrases = [
        f"I would try and describe it to you, but when I looked at {usr.mention}, I was blinded by their beauty. Like it was so bright I thought I was dying.",
        "Bro is gorgeous :skull:",
        f"Just be careful when {usr.mention} takes their shirt off. You might give up on ever going to the gym.",
        f"We don't talk enough about how cute {usr.mention} is if we're being honest.",
        f"You KNOW you're staring at {usr.mention} when they walk into the room. Don't lie :wink:",
        f"{usr.mention} has the clearest skin and most gorgeous hair ever. Wouldn't be surprised if they end up modeling (just know that I called it)",
        "Bro is resplendent :skull:",
        "Bro is prepossessing :skull:"
    ]

    await ctx.channel.send("Ugly" if rnd.random() <= 0.01 else phrases[rnd.randint(0, len(phrases) - 1)])


#Decorator to specify this is triggered by an event, the event being a message sent
#In other words, this checks every message sent.
@bot.event
async def on_message(msg):
    await bot.process_commands(msg)
    if msg.author.id == 9999999999999:
        return
        # await msg.reply('')
    else:
        return


bot.run(TOKEN)
