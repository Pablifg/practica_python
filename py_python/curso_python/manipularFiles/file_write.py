# Cuando usar open(), por default vienen SOLO PERMISOS de LECTURA
with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    # Escribir en el archivo
    file.write("New thing in this file\n")
    file.write("New line\n")
    file.write("New line\n")

'''
Permisos:
-- r+: permite leer y escribir. Orientado a agregar nuevas líneas, respetar lo que el contenido tiene y a AGREGAR MÁS.
-- w+: permisos de lectura y escritura. Va a SOBREESCRIBIR todo el archivo.
'''