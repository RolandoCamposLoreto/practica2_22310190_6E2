""" ordenamiento tipo baraja de cartas """

def insertion_sort(lista): """Ordena una lista que usa el algoritmo InsertionSort (Insercion)"""
lista = 1,5,3,2,4
for i in range(1, len(lista)): """aqui recorre la lista  """
clave = lista[i] 
"""almacena el valor del elemento actual que se esta ordenando"""
j = i - 1
while j>= 0 and clave < lista[j]: """compara el valor almacenado con los anteriores de derecha a izquierda"""
lista[j + 1] = lista[j]
j -= 1
lista[j + 1] = clave 
"""inserta clave en su posicion correcta"""

"""en la lista se acomoda clave donde si esta es menor que el elemento anterior comparado osea listaj se desplaza
al elemento anterior una posicion a la derecha hasta que se encuentre la posicion correcta"""
