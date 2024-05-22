# Manejo de Excepciones en Python

## Excepciones

En Python cuando el intérprete detecta algún tipo de error (algo que no puede solucionar en tiempo de ejecución) se activa mecanismo que lanza excepción.

Si la excepción no es maneja de forma correcta, finaliza el programa de forma abrupta.

Para manejar excepciones usaremos:
```
try:
    <code>
except:
    <code>
```
- En **try** colocaremos todo el código que creamos pueda ocasionar un tipo de error
- En **except** colocamos plan B, comportamiento una vez falle el try

#### Tipos de errores
Existen muchos tipos de errores, como errores de:
- Sintáxis
- Identación
- ZeroValue
- Importar módulos
- Declarar Variables
- Leer archivos
- De memoria
- Etc

" Todos los errores responden a orden jerárquico, a través de clase padre _BASE EXCEPTION_ que se crean resto de excepciones.
- De tal manera podemos trabajar las excepciones de manera individual o grupal
#### Considerar
- En python todos los errores son excepciones
- No todas las excepciones son errores
- Podemos lanzar nuestras propias excepciones

## Traceback
Rastreo de ejecución (Traceback) es una lista de llamadas y excepciones que se muestra cuando ocurre un tipo de error.
- Permite conocer información detallada sobre secuencia de eventos que conducieron al error. 
  - Facilita la depuración y diagnóstico de problemas en el código
- Si la excepción no es manejada de forma correcta python muestra Traceback desde donde se generó la excepción hasta nivel más alto de la pila de llamadas.
#### Contenido de entrada del traceback
- Archivo
- Línea
- Nombre de la función donde se produjo la llamada
#### Conclusión
- Traceback solo se genera cuando se produce una excepción no manejada
- Fundamenal para rastrear y diagnosticar error
- Proporciona información detallada sobre las llamadas y excepciones que condujeron al error

## Bloques Opcionales
Tenemos 2 bloques opcionales en el manejo de excepciones:
- else
  - Se ejecuta sí y solo sí el _try_ se ejecutó sin problema (no ocurrió error)
- finally
   - Se ejecuta siempre (ocurra o no un error)
#### Estructura
```
try:
    <somethin>
except:
    <somethin>
else:
    <something>
finally:
    <something>
```
