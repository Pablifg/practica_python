# CÓDIGO QUE IRÁ A PRODUCCIÓN
def calculate_total(products):
    """Función que calcula total de producto
    """
    total = 0
    for product in products:
        total += product["price"]
    return total

# PRUEBAS PARA VALIDAD QUE LUEGO DE HACER UN CAMBIO LA 
# FUNCIONALIDAD SIGA IGUAL QUE AL CONSTRUIR PRIMERA VEZ
# DONDE FUNCIONABA CORRECTAMENTE
#Probar función
def test_calculate_total_with_empty_list():
    print("Testing ... Empty list")
    #1er test: validamos que es 0 si lista está vacía
    assert calculate_total([]) == 0 # condicion debe dar verdadero con el assert

def test_calculate_total_with_single_product():
    # Queremos probar que suma de valor correctp
    print("Testing ... Single Product")
    products = [
        {
            "name": "Notebook",
            "price": 5
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product():
    # Queremos probar que suma de valor correctp
    print("Testing ... Multiple Product")
    products = [
        {
            "name": "Notebook", "price": 15
        },
        {
            "name": "Book", "price": 3
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products) == 20

    
if __name__ == '__main__':
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()