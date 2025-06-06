"""encuentra el elemento mas pequeño y lo acomoda en la lista en su posicion correcta"""

def selection_sort(lista):
    lista = 1,3,6,8,2,5,7
    n = len(lista)
    for i in range(n):
        #asume el elemento esta en el valor minimo 
     min_index= i 
        #busca el valor minimo en la parte no ordenada
     for j in range(i + 1, n):
        if lista[j] < lista[min_index]:
           min_index = j
        # Intercambia el valor minimo con el elemento en la posicion actual hasta ordenar toda la lista
    lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista 