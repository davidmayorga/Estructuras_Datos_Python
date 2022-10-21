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
lista = lista + ["Abrigo"]
print(lista)
lista = lista +["Jersey", "Sudadera"]
print(lista)
lista = lista +["Calcetines"]+["Bufanda"]
print(lista)

# 4. Modifica elementos de una lista y borrar elementos de la misma 
lista = ["Camiseta", "Pantalon", "Zapatilla"]
print(lista)
lista[1] = "Cazadora"
print(lista)

# 5. Uso del operador *. Permite concatenar una lista con ella misma u número finito de veces.
lista = ["Camiseta", "Pantalon", "Zapatilla"]
print(lista)
lista_resultante = lista * 3
print(lista_resultante)

# 6. Creación de listas como elementos de listas y acceso a dichos elementos.
print("......Ejercicio 6......") 
lista = ["Camiseta", ["Calcetines","Cazadores"], "Zapatillas"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])

# 7. Extraer una porcion de la lista en una lista nueva 
print("......Ejercicio 7......") 
lista = [1,2,3,4,5,6,7,8,9]
print(lista)
lista1 = lista[3:7]
print(lista1)
lista2 = lista[:5]
print(lista2)
lista3 = lista[6:]
print(lista3)