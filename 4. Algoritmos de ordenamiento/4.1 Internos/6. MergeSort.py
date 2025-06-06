form array import array
def ordenar(lista):
    tamano_de_lista= len(lista) -1 
    for posicion_actual in range(0, tamano_de_lista):
        posicion_menor = posicion_actual
        nombre_menor = lista[posicion_menor]
        for posicion_buscar in range(posicion_actual, tamano_de_lista):
            nombre_buscar = lista[posicion_buscar + 1]
            if nombre_menor 