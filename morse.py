
"""Code for python"""

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'a': '·−', 'b': '−···', 'c': '−·−·', 'd': '−··', 'e': '·',
    'f': '··−·', 'g': '−−·', 'h': '····', 'i': '··', 'j': '·−−−',
    'k': '−·−', 'l': '·−··', 'm': '−−', 'n': '−·', 'o': '−−−',
    'p': '·−−·', 'q': '−−·−', 'r': '·−·', 's': '···', 't': '−',
    'u': '··−', 'v': '···−', 'w': '·−−', 'x': '−··−', 'y': '−·−−',
    'z': '−−··', '0': '−−−−−', '1': '·−−−−−', '2': '··−−−−−',
    '3': '···−−−−', '4': '····−−−', '5': '·····', '6': '−····',
    '7': '−−···', '8': '−−−··', '9': '−−−−·', ' ': ' '
}

def clean_sentence(sentence):
    # Convert to lowercase and remove unwanted characters.
    return ''.join(char for char in sentence.lower() if char in MORSE_CODE_DICT)

def sentence_to_morse(sentence):
    # Convert a cleaned sentence to a list of Morse code.
    morse_list = []
    for char in sentence:
        if char in MORSE_CODE_DICT:
            morse_list.append(MORSE_CODE_DICT[char])
            morse_list.append(' ')  # Space between characters
    morse_list.append('       ')  # Space between words
    return morse_list

def main():
    user_input = input("Enter a sentence: ")
    cleaned_sentence = clean_sentence(user_input)
    morse_code_list = sentence_to_morse(cleaned_sentence)
    print("Morse Code Representation:", ' '.join(morse_code_list))

if __name__ == "__main__":
    main()


    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////

    """Code for the circuit playground"""

    import time
from adafruit_circuitplayground import cp

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'a': '·−', 'b': '−···', 'c': '−·−·', 'd': '−··', 'e': '·',
    'f': '··−·', 'g': '−−·', 'h': '····', 'i': '··', 'j': '·−−−',
    'k': '−·−', 'l': '·−··', 'm': '−−', 'n': '−·', 'o': '−−−',
    'p': '·−−·', 'q': '−−·−', 'r': '·−·', 's': '···', 't': '−',
    'u': '··−', 'v': '···−', 'w': '·−−', 'x': '−··−', 'y': '−·−−',
    'z': '−−··', '0': '−−−−−', '1': '·−−−−−', '2': '··−−−−−',
    '3': '···−−−−', '4': '····−−−', '5': '·····', '6': '−····',
    '7': '−−···', '8': '−−−··', '9': '−−−−·', ' ': ' '
}

def clean_sentence(sentence):
    """Convert to lowercase and remove unwanted characters."""
    return ''.join(char for char in sentence.lower() if char in MORSE_CODE_DICT)

def sentence_to_morse(sentence):
    """Convert a cleaned sentence to a list of Morse code."""
    morse_list = []
    for char in sentence:
        if char in MORSE_CODE_DICT:
            morse_list