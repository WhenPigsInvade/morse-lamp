import time
from gpiozero import LED

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

# Function to encrypt the string
# according to the morse code chart
def translate_to_morse(message: str):
    message = message.upper()
    cipher = ""
    for letter in message:
        if letter != " " and letter in MORSE_CODE_DICT.keys():

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += " "

    return cipher


# Hard-coded driver function to run the program
def morse_led(morse_code: str):
    pause = 60 / 750  # 60/(dit per word / wpm) --> 60/(50 *15)

    led = LED(18)

    for char in morse_code:

        if char == ".":
            led.on()
            time.sleep(pause)
            led.off()
            time.sleep(pause)

        elif char == "-":
            led.on()
            time.sleep(pause)
            time.sleep(pause)
            time.sleep(pause)
            led.off()
            time.sleep(pause)

        elif char == " ":
            time.sleep(7 * pause)
