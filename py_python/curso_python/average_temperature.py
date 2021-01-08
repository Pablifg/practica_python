# -*- coding: utf-8 -*-

def average_temp(temps):
    sum_temps = 0

    for temp in temps:
        sum_temps += float(temp)
    
    return round(sum_temps / len(temps), 2)


def run(temps):
    average = average_temp(temps)
    
    print(f'The average temperature is: {average}')


if __name__ == '__main__':
    temps = [21, 23, 19, 20, 24, 23, 22]
    run(temps)
