items = [
    {
        'product': 'camisa',
        'price': 100,
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantalones 2',
        'price': 200
    }
]

# TRANSFORMAR PARA OBTENER LISTA DE LOS PRECIOS
prices = list(map(lambda item: item['price'], items))
print(f'Hay 3 dictionarios, tenemos 3 números de elementos(precios): {prices}')

# AGREGAR ATRIBUTO NUEVO A DICCIONARIO
## Al tener mayor complejidad no es suficiente con usar lambda function, para ello uso: funciones
def add_taxes(item):
    item = item.copy() # solución a modificación del array original llamado 'items'. Variable local. Ayuda a 'Quita referencia en memoria'
    item['taxes'] = item['price'] * 0.19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
print("")
print(items)
