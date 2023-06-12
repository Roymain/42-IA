from load_csv import load
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    try:
        path_strg = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        matplotlib.use('webagg')
        df_inc = load(path_strg)
        if "None" in str(type(df_inc)):
            return 1
        df_life = load("life_expectancy_years.csv")
        if "None" in str(type(df_life)):
            return 1
        df_inc = pd.DataFrame(df_inc)
        df_life = pd.DataFrame(df_life)

        df_inc = df_inc.rename(columns={"1900": "inc"})
        df_life = df_life.rename(columns={"1900": "life"})
        df_final = pd.concat([df_inc, df_life], axis=1, join='inner')
        df_final = df_final.dropna()

        fig = plt.figure()
        ax = fig.add_subplot(111)
        xpoints = np.array(df_final["inc"])
        ypoints = np.array(df_final["life"])

        plt.plot(xpoints, ypoints, 'o')

        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")

        ax.set_xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

        plt.title("1900")
        plt.show()

    except AssertionError as msg:
        print(msg)


main.__doc__ = "plot gross domestic product and\
     life exepectancy of all country"


if __name__ == "__main__":
    main()
