import sys
from string import punctuation


def main():
    print(punctuation)
    punct = "!\"#$%&'()*+,-./:;<=>?@[]\\^_`{|}~"
    if len(sys.argv) == 1:
        string = input("What is the text to count?\n")
        arg = string
    else:
        arg = sys.argv[1]
    try:
        assert len(sys.argv) < 3, "only one argument pls"
        print("The text contains", len(arg), "characters:")
        print(sum(1 for a in arg if a.isupper()), "upper letters")
        print(sum(1 for a in arg if a.islower()), "lower letters")
        print(sum(1 for a in arg if a in punct), "punctuation marks")
        print(arg.count(' '), "spaces")
        print(sum(1 for a in arg if a.isnumeric()), "digits")

    except AssertionError as msg:
        print(msg)


main.__doc__ = "count all char: uppercase, lowercase, punctuation\
, spaces, digits"

if __name__ == "__main__":
    main()
