import sys


def main():  
    try:
        assert len(sys.argv) <= 2, "more than one argument are provided"
        if len(sys.argv) == 1:
            return 0
        if sys.argv[1][0] == '-' and sys.argv[1].count('-') == 1:
            sys.argv[1] = sys.argv[1].replace("-", "0")
        assert sys.argv[1].isnumeric() == True, "argument is not an integer"
        val = int(sys.argv[1])
        if val % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    
    except AssertionError as msg:
        print(msg)

if __name__ == "__main__":
    main()