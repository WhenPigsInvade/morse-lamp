import discord
import threading
from discord.ext import commands
from queue import Queue

from morse import morse_led, translate_to_morse

bot = commands.Bot(command_prefix="!")
job_queue = Queue(maxsize=10)

filtered = set()
with open("filter.txt", "r") as file:
    for word in file.readlines():
        filtered.add(word.strip())


@bot.command()
async def morse(ctx, *, message):
    await ctx.send(translate_to_morse(message))


@bot.command()
async def lamp(ctx, *, message):
    if job_queue.full():
        await ctx.send("Job queue is full, please try again later")

    else:
        text = ctx.message.content[5:]
        blocked = filter(text.lower().split())
        if not blocked:
            text = translate_to_morse(text)
            job_queue.put(text)
            await ctx.send("Added to queue: " + message)

        else:
            await ctx.send("Word blocked: " + blocked)


def filter(text):
    blocked = ""
    for word in text:
        if(word in filtered):
            blocked = word
    return blocked


def job():
    if job_queue.empty() is False:
        morse_led(job_queue.get())
    job()


threading.Thread(target=job, daemon=True).start()

with open("token.txt", "r") as file:
    token = file.read().splitlines()[0].strip()
bot.run(token)
