# EJERCICIOS LISTAS

#Ejercicios manipulacion 

#1. Consiste en la definicion de una lista con elementos de diferentestipos y en mostrarla por pantallas, tanto entera como por elementos accediendo a la posicíon que ocupa dentro del area 
lista = ["Python", "Guanenta", 2022, "Libro", 3]
print(lista)
print(lista[0])
print(lista[2])

# 2. Consise en el uso del operador + para realizar uniones de listas. Ademas, utilizar la funcion len para conocer el numero de elementos que componen la lista.
lista1 = ["Camiseta0", "Pantalon", "Zapatilla"]
lista2 = ["Abrigo", "Jersey", "Sudadera", "Calcetines"]
print("Numero de elementos lista1: ", len(lista1))
print("lista1: ", lista1)
print("Numero de elementos lista2: ", len(lista2))
print("lista1: ", lista2)
lista_concatenada = lista1 + lista2
print("Numero de elementos lista_concatenada: ", len(lista_concatenada))
print("lista_concatenada: ", lista_concatenada)

# 3. Añadir elementos a la lista de diferentes formas
lista = ["Camiseta", "Pantalon", "Zapatilla"]
print(lista)
lista = lista + ("Abrigo")
print(lista)
lista = lista +("Jersey", "Sudadera")
print(lista)
lista = lista +("Calcetines")+("Bufanda")
print(lista)

# 4. Modifica elementos de una lista y borrar elementos de la misma 
lista = ["Camiseta", "Pantalon", "Zapatilla"]
print(lista)
lista[1] = "Cazadora"
print(lista)


