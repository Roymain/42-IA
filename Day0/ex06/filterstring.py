import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "only 2 arguments pls"
        assert sys.argv[2].isnumeric() is True, "the arguments are bad"
        size = int(sys.argv[2])
        data = sys.argv[1].split()
        newlist = list(ft_filter((lambda a: len(a) > size), data))
        print(newlist)
    except AssertionError as msg:
        print(msg)


main.__doc__ = "return a list of words in first ARG1 \
that contains more than ARG2 characters"

if __name__ == "__main__":
    main()
