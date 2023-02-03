import utils
'''
Other example to access:
    from utils import get_population 

    Ex:
        keys, values = get_population()
        print(keys, values)
'''

data = [
    {
        'country': 'Colombia',
        'Population': 500
    },
    {
        'country': 'Ecuador',
        'Population': 250
    },
    {
        'country': 'Argentina',
        'Population': 350
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    print(utils.A)

    country = input('Type Country => ')

    result = utils.population_by_country(data, country)
    print(result)


if __name__ == '__main__':
    #print(__name__)
    run()