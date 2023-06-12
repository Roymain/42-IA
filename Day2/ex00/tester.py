from load_csv import load


def main():
    try:
        print(load("life_expectancy_years.csv"))
        print(load.__doc__)

    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
