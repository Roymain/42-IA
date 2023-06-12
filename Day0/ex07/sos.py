import sys


def main():
    MORSE_CODE_DICTT = {' ': "/ ", 'A': '.-', 'B': '-...',
                        'C': '-.-.', 'D': '-..', 'E': '.',
                        'F': '..-.', 'G': '--.', 'H': '....',
                        'I': '..', 'J': '.---', 'K': '-.-',
                        'L': '.-..', 'M': '--', 'N': '-.',
                        'O': '---', 'P': '.--.', 'Q': '--.-',
                        'R': '.-.', 'S': '...', 'T': '-',
                        'U': '..-', 'V': '...-', 'W': '.--',
                        'X': '-..-', 'Y': '-.--', 'Z': '--..',
                        '1': '.----', '2': '..---', '3': '...--',
                        '4': '....-', '5': '.....', '6': '-....',
                        '7': '--...', '8': '---..', '9': '----.',
                        '0': '-----', ', ': '--..--', '.': '.-.-.-',
                        '?': '..--..', '/': '-..-.', '-': '-....-',
                        '(': '-.--.', ')': '-.--.-'}
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        for x in sys.argv[1]:
            if x == ' ' or x.isalnum():
                continue
            else:
                assert False, "the arguments are bad"
        up = sys.argv[1].upper()

        txt = ""
        for a in up:
            txt += MORSE_CODE_DICTT.get(a)
        print(txt)

    except AssertionError as msg:
        print(msg)


main.__doc__ = "Convert a string in Morse"

if __name__ == "__main__":
    main()
