# EJERCICIOS LISTAS 

# Métodos propios
lista = [45, 32,3,78]
print("lista original: ", lista) 
# Funcion append: añade un elemento a la lista 
lista.append(995)
lista.append(7)
print("Lista desoues de usar append: ", lista)
# Funcion sort:  Ordena la lista.
lista.sort()
print("Lista ordenada: ", lista)
# Funcion reverse: Invierte el orden de la lista 
lista.reverse()
print("Lista al revés: ", lista)

# Función extend: Añade los elementos de una lista a la lista 
lista_extend =[1,5,87,45]
lista.extend(lista_extend)
print("Lista despues de extend: ", lista)

# Funcion count: Cuenta el numero de veces que aparece el elemento indicado como parametro dentro de la lista 
print("Numero de elementos 45: ", lista.count(45))
# Funcion insert: Añade el elemento pasado como parametro a la lista en la posicíon indicada también por parámetro 
lista.insert(3,111)
print("Lista desoues de insert: ", lista)
# Funcion remove: Elimina la primera oocurrencia empezando por la izquierda de la lista del elemento indicado como parámetro
lista.remove(45)
print("Lista despues de remove: ", lista)
# Funcion index: Devuelve la posición de la primera ocurrencia de izquierda a derecha en la lista,del elemento pasado como parámetro 
print("Posición del elemento 111: ",lista.index(111))
# Funcion pop: Elimina el ultimo elemento de la lista y lo devuelve como resultado de la operación
lista.pop()
print("Lista despues del pop: ", lista)
# Funcion clear: Elimina todos los elementos de la lista t
lista.clear()
print("Lista despues de clear: ", lista)