import utils
import read_csv
import charts
'''
Other example to access:
    from utils import get_population 

    Ex:
        keys, values = get_population()
        print(keys, values)
'''

def run():
    data = read_csv.read_csv("./data.csv")
    country = input('Type Country => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)

    print(result)


if __name__ == '__main__':
    run()