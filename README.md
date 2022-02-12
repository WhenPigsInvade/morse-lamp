# Morse-Lamp
Discord Bot which translate text and flashes morse code from a LED lamp.

## Table of Contents
* [Introduction](#introduction)
* [Installation](#installation)
* [Configurations](#configurations)
* [Change Log](#change-log)

## Introduction
Morse-lamp takes input from a Discord text channel and uses GPIO on Raspberry Pi to output morse code.

## Installation
To run Morse-lamp you will need a Raspberry Pi with GPIO Pins

1. Then install the following libraries:
    * Discord.py `pip install discord.py`
    * gpiozero `pip install gpiozero`

2. Connect the LED light to the GPIO pin

       Positive to pin 12
       Negative to pin 6
       
       *Reminder that the longer end is positive
  
3. Run main.py `python main.py`

## Configurations

Currently Morse-lamp only has the following commands

* `!morse` which replies with the message in morse code
* `!lamp` sends the morse code of the message to the LED

Text filter list and message recipt when message is broadcasted will be added soon.

## Change log
2/11/2021 - Initial Release
