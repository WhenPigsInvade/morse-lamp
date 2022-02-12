from gpiozero import LED
import time
import discord
import threading
from discord.ext import commands
from queue import Queue

bot = commands.Bot(command_prefix='!')
jobq = Queue(maxsize = 10)

@bot.command()
async def morse(ctx):
    await ctx.send(encrypt(ctx.message.content[6:]))

@bit.command()
async def lamp(ctx):
    if(jobq.full()):
        await ctx.send("Job queue is full, please try again later")
    
    else:
#        jobq.put(encrypt(ctx.message.content[6:]))
        text = encrypt(ctx.message.content[5:])
        jobq.put(text)
        #main(encrypt(ctx.message.content[5:]))
        await ctx.send("Added to queue: "+ ctx.message.content)

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
 
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    message = message.upper()
    cipher = ''
    for letter in message:
        if letter != ' ' and letter in MORSE_CODE_DICT.keys():
 
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher

# Hard-coded driver function to run the program
def main(morse_code):
    pause = 60/750 # 60/(dit per word / wpm) --> 60/(50 *15)
        
    led = LED(18)

    for char in morse_code:


        if(char == '.'):
            led.on()
            time.sleep(pause)
            led.off()
            time.sleep(pause)
        
        if(char == '-'):
            led.on()
            time.sleep(pause)
            time.sleep(pause)
            time.sleep(pause)
            led.off()
            time.sleep(pause)

        if(char == ' '):
            time.sleep(pause)
            time.sleep(pause)
            time.sleep(pause)
            time.sleep(pause)
            time.sleep(pause)
            time.sleep(pause)
            time.sleep(pause)

def job():
    while true:
        if(!jobq.empty():
           main(jobq.get())

job_thread = threading.Thread(target=job)

job_thread.start()

#main_thread = threading.Thread(target=main)

with open("token.txt", "r") as file:
    token = file.read().splitlines()[0].strip()
bot.run(token)
