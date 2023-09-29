# funcion principal para determinar la similitud de los textos
def similitud(palabra1, palabra2):
    # conversion del texto '1' en binario
    binario1 = ''.join(format(ord(char), '08b') for char in palabra1)
    # conversion del texto '2' en binario
    binario2 = ''.join(format(ord(char), '08b') for char in palabra2)

    # calcular cual de los dos binarios es el de mayor longitud
    maximo_long = max(len(binario1), len(binario2))
    # justificar a la izquierda el binario '1' y '2'
    # con el metodo ljust(). Si la cadena es menor al maximo_long,
    # se llenara con 0 a la derecha
    binario1 = binario1.ljust(maximo_long, '0')
    binario2 = binario2.ljust(maximo_long, '0')


    # Realizar la operación XOR y contar cuántos bits son iguales
    #se inicia la variable similares con 0
    similares = 0
    #metodo zip() para comparar cada caracter de la cadena
    for c1, c2 in zip(binario1, binario2):
        # si son iguales entonces, se adiciona +1 a la variable similares
        if c1 == c2:
            similares += 1
        
    # calcular el porcentaje con la formula proporcionada
    porcentaje_similitud = (similares / maximo_long) * 100
    
    #fin de la funcion
    return porcentaje_similitud
 
   
# definimos dos textos
palabra1 = "Microprocesadores"
palabra2 = "Microcontroladores"
similitud = similitud(palabra1, palabra2)
redondeado_similitud = round(similitud, 4)
print(f"Porcentaje de similitud: {redondeado_similitud}%")






# OPERACION XOR

"""
    A           B            A XOR B
    0           0               0
    0           1               1
    1           0               1
    1           1               0
"""






