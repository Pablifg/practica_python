import copy

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
    #item = item.copy() # solución a modificación del array original llamado 'items'. Variable local
    item['taxes'] = item['price'] * 0.19
    return item
'''
new_items = list(map(add_taxes, items))
print(new_items)
print("")
print(items)
'''
items_2 = copy.deepcopy(items)
print("")
print("*" * 10)
print("")

# OTRAS POSIBLES SOLUCIONES
newItems = list(map(lambda item: {**item, 'tax':item['price'] * 0.19}, items))
# "**": para desempaquetar diccionario [su uso es muy variado. Leer documentación]
print(newItems)
print("")
print(items)

print("")
print("*" * 10)
print("")
print(items_2)    
newItems_v2 = list(map(lambda item: add_taxes(item), items_2)) # Funciona si hacemos copy en item de la función add_taxes
print(newItems_v2)
print("")
print(items)
print(items_2) # Ah funcionado el deepcopy. Se modifica items_2 pero no items [original]