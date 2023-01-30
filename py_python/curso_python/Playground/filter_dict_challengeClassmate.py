'''
Tenemos una lista de estudiantes de la cual debemos saber quienes son de Colombia
y quienes son considerados mayores de edad al tener igual o mas de 18 años y cuantos son.
'''

people = [
    {
        'name': 'Pedro',
        'country': 'Colombia',
        'age': 18,
        'course': 'developer'
    },
    {
        'name': 'Juan',
        'country': 'Perú',
        'age': 17,
        'course': 'UX'
    },
    {
        'name': 'Carlos',
        'country': 'Chile',
        'age': 31,
        'course': 'Diseño'
    },
    {
        'name': 'Ana Maria',
        'country': 'Colombia',
        'age': 25,
        'course': 'Tester'
    }
]

# 1. Estudiantes de colombia
print("Estudiantes de Colombia")
country = list(filter(lambda item: item['country'] == 'Colombia' ,people))
print(country)
print(len(country))
print('\n ******************* \n')

# 2. Quienes son mayores de edad
adult = list(filter(lambda item: item['age'] >= 18,people))
print(adult)
print(len(adult))
print([adult[i]['name'] for i in range(len(adult))])