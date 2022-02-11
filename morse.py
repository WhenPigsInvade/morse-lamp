from gpiozero import LED
import time
# Python program to implement Morse Code Translator
# Text to morse from Geeks4geeks
'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''
 
# Dictionary representing the morse code chart
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
def main():
    with open('text.txt', 'r') as reader:
        results = reader.read()
        results = results.upper()

        print(results)
        results = encrypt(results)
        print(results)

        pause = 60/750 # 60/(dit per word / wpm) --> 60/(50 *15)
            
        led = LED(18)

	for char in results:


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


# Executes the main function
if __name__ == '__main__':
    main()
