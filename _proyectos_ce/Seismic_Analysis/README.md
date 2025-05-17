## Proyecto - Análisis sísmico de un edificio
**Objetivo:** APlicar los conocimientos de Python en el análisis símico en edificaiones

**Problema**:
- Del modelo de un edificio de 5 pisos, se obtuvieron los periodos y las formas de vibración de los 3 modos de vibración. LA estructura del edifico es aporticada de concreto armado (hormigòn armado) y tiene la configuración regular. El edificio cuenta con una altura típica de lso pisos en 3m. Se pide realizar el análisis dinámico modal espectral para obtener el diagrama de fuerzas cortantes real por piso.

- La masa tiene unidades de: $\frac{t*s^2}{m}$
- El Periodo de la estructura en cada modo de vibración: s
- Los modos de vibración ya estàn normalizados con respecto a la matriz de masas.

**Consideraciones adicionales**:
- T aprox del edificio està representado por la altura total del edificio divido por un coeficiente (ct) cuto valor es 35 para el caso de edificios aporticados.
- La pseudo-aceleración espectral (Sa) se representa por la gravedad multiplicada por un factor ZUCS/R. Donde Z=45 (factor de zona sísmica), U=1.0 (factor de uso para edificios comunes), S=1.0 (factor de amplificación dle suelo), y R=8 (factor de reducción de fuerza sísmica)
- El factor C de amplificación sísmica se calcula de la siguiente forma (Tp=0.4s, TL=2.5s, y T es el periodo correspondiente al modo de vibración):
$$
T<T_P ----- C=2.5
TP<T<T_L----C=2.5*\frac{T_P}{T}
T>T_L-------C=2.5*\frac{T_P*T_L}{T^2}
$$
- La frecuencia estructural W de cada modo de vibración se calcula como: $\frac{2*pi()}{T}$
...... continuará



## Solución:
1. seismicAnalysis --> contiene funciones para desarrollar el análisis sísmico