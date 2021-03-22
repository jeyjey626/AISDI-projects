import sys

# Morse code table, according to lab document
MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..', 'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---', 'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-', 'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..'
              }


def morse_code():
    text = open(sys.argv[1]).read()  # reading file
    final_message = ''

    for char in text:
        if MORSE_CODE.get(char.upper()):  # adding the char from code table
            final_message += MORSE_CODE[char.upper()] + ' '
        elif char == ' ' and not final_message.endswith('/ '):  # swapping only one space in between chars
            final_message += "/ "
        elif char == '\n':  # preserving line  breaks
            final_message += char

    final_message = final_message[:-1]  # removing last space
    print(final_message)


if __name__ == '__main__':
    morse_code()


