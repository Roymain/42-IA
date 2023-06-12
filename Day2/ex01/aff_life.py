from load_csv import load
import matplotlib
import matplotlib.pyplot as plt


def main():
    try:
        matplotlib.use('webagg')
        df_le = load("life_expectancy_years.csv")
        if "None" in str(type(df_le)):
            return 1

        df_le = df_le.drop(['country'], axis=1)
        row = df_le.loc[58]
        row = row.to_frame()

        print(row)

        plt.plot(row)
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.xticks(["1800", "1840", "1880", "1920", "1960", "2000",
                    "2040", "2080"])
        plt.title("France life expectancy projection")
        plt.show()

        return 0

    except AssertionError as msg:
        print(msg)


main.__doc__ = "plot life exepectancy per year in France"


if __name__ == "__main__":
    main()
