from load_csv import load
import csv
import matplotlib
import matplotlib.pyplot as plt


def select_country(name: str):

    with open("population_total.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for line in enumerate(reader):
            if "country" in line[1][0]:
                years = line[1][0]
            if name in line[1][0]:
                country_line = line[1][0]
    lst_year = years.split(',')
    lst_pop = country_line.split(',')
    lst_year.remove("\ufeffcountry")
    lst_pop.remove(name)
    year = [float(i) for i in lst_year if float(i) <= 2050]
    pop = list()
    for x in lst_pop:
        if 'K' in x:
            x.replace("K", "")
            pop.append(float(x))
        if 'M' in x:
            x = x.replace("M", "")
            pop.append(float(x) * 1000)
        if 'B' in x:
            x = x.replace("M", "")
            pop.append(float(x) * 1000000)

    while len(pop) > len(year):
        pop.pop()

    return year, pop


select_country.__doc__ = "convert K M B in a csv"


def main():
    try:
        matplotlib.use('webagg')
        test = load("population_total.csv")
        if "None" in str(type(test)):
            return 1
        lst_year, lst_fr = select_country("France")
        lst_year, lst_be = select_country("Belgium")
        plt.plot(lst_year, lst_be, color='blue')
        plt.plot(lst_year, lst_fr, color='green')
        plt.xlabel("Year")
        plt.ylabel("population")
        plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040])
        plt.yticks([0, 20000, 40000, 60000], ['', '20M', '40M', '60M'])

        plt.title("Population projection")
        plt.show()

    except AssertionError as msg:
        print(msg)


main.__doc__ = "plot France and Belgium pop per year"


if __name__ == "__main__":
    main()
