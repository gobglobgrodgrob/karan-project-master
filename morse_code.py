'''
Created on 10/04/2016

@author: Nick
'''

"""
Converts a string into morse code.
"""


Code = {'A': '.-', 'B': '-...', 'C': '-.-.', 
 'D': '-..', 'E': '.', 'F': '..-.',
 'G': '--.', 'H': '....', 'I': '..',
 'J': '.---', 'K': '-.-', 'L': '.-..',
 'M': '--', 'N': '-.', 'O': '---',
 'P': '.--.', 'Q': '--.-', 'R': '.-.',
 'S': '...', 'T': '-', 'U': '..-',
 'V': '...-', 'W': '.--', 'X': '-..-',
 'Y': '-.--', 'Z': '--..',
 
 '0': '-----', '1': '.----', '2': '..---',
 '3': '...--', '4': '....-', '5': '.....',
 '6': '-....', '7': '--...', '8': '---..',
 '9': '----.', ' ': ''
        }

def main():
    message = raw_input('Enter your message: ')

    for i in message:
        print (Code[i.upper()]),

if __name__ == "__main__":
    main()
