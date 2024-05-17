# Anotaciones y Type Hints

## Anotaciones
Permite definir el tipo de datos que usaremos para cada una de las variables, mediante la anotación ":"
```
a : int = 10
b : float = 3.14
c : bool = False
d : str = 'Codigo'
```

Las usamos en 4 áreas principalmente:
- Variables
- Colecciones
- Funciones
- Clases

Usar anotaciones mejorar claridad y legibilidad del código.

Es una ayuda para el usuario que codifica, NO PARA EL INTÉRPRETE


## Type Hints
Son opcionales y no afectan al comportamiento en tiempo de ejecución


### Any y TypeVar
- Any: una varible puede ser de cualquier tipo. No realiza ninguna verificación de tipo.
- TypeVar: crear variables de tipo genérico. Indica que tipo es desconocido o puede variar.

Conclusión:
- **TypeVar**: se usa para crear variables de tipo genérico
- **Any**: se usa para indicar que _Any_ puede ser de cualquier tipo y se deshabilita la comprobación de tipos para esas variables
