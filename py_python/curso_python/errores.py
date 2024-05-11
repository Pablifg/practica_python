# -*- coding: utf-8 -*-

countries = {
        'mexico': 122,
        'colombia': 49,
        'ecuador': 17,
        'argentina': 43,
        'chile': 18,
        'peru': 31
}

while True:
    country = input('Write the country\'s name: ').lower()
    
    #Encapsular llamada dentro de bloque try
    try:
        print(f'The poblation of {country} is: {countries[country]}')
    except KeyError:
        print(f'There aren\'t the date of country: {country}')
    finally:
        exit = int(input('Do you want exit?:\n[0] Yes \n[1] No'))
        if exit == 0:
            break
