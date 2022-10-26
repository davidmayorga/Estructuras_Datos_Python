# Tanto en las listas como en las tuplas, los elementos empiezan por la posición 0, no por la 1 como pareceria lo obvio. Tenlo en cuenta cuando utilices tuplas.

tupla =("Casa", "2",345, "Perro",99) 
print("Elementos de la tupla: ", tupla)
print("Elemento de la posición 0: ", tupla[0]) 
print("Elemento de la posición 1: ", tupla[1]) 
print("Elemento de la posición 2: ", tupla[2]) 
print("Elemento de la posición 3: ", tupla[3]) 
print("Elemento de la posición 4: ", tupla[4]) 

#  funcion count: cuenta el número de veces que aparece el elemento indicado como parámetro dentro de la tupla.
#  funcion index: devuelve la posición de la primera ocurrencia de izquierda a derecha en la tupla del elemento pasado como parámetro.

#  vamos realizar un ejercicio para aprender a utilizar ambas funciones de las tuplas.
tupla = ('Casa', '2',99, 345, 'Perro',99)
print("Elementos de la tupla: ", tupla) 
print("Número de elementos 99: ", tupla.count (99)) 
print("Posición que ocupa el elemento Perro: ", tupla.index("Perro"))

#  funcion tupla[n:m]: La instrucción extraerá una nueva tupla que empezará en el indice ny terminará en el m-1. 

tupla = (1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla[4:9])
print(tupla[:3])
print(tupla[2:])

#  funcion tupla concatenada "+" :  esta función se llama len(Tupla) y devuelve un entero que indica el número de elementos que la componen. Se utiliza de la siguiente manera:

tupla1= (29, "Televisión", 8763)
tupla2 =(1,2,3, "Videojuego") 
print("Número elementos de tupla1: ",len (tupla1)) 
print("Tupla1: ", tupla1) 
print("Numero elementos de tupla2: ", len(tupla2)) 
print("Tupla2: ", tupla2) 
tuplaconcatenada =tupla1+ tupla2 
print("Numero elementos de tuplaconcatenada: ",len (tuplaconcatenada)) 
print("tuplaconcatenada: ", tuplaconcatenada)

# funcion Tupla Resultante "*" : La tupla resultante de la multiplicación será una tupla compuesta por tantas veces la Tupla como valor tenga el número entero.

tupla = (1,2,3,4,5,6,7,8,9,0) 
print(tupla) 
tuplaresultante = tupla* 4 
print(tuplaresultante)


# NumeroElementos = len(tupla): el uso de operador "+" esto nos permite realizar uniones de tuplas, el operador se usa de la siguiente manera tuplaconcatenada = tupla1+ tupla2
tupla1 = (29, "Televisión", 8763)
tupla2 = (1,2,3, "Videojuego")
print("Número elementos de tuplal: ", len(tupla1))
print("Tuplal: ", tupla1)
print("Número elementos de tupla2: ", len(tupla2))
print("Tupla2: ", tupla2)
tuplaconcatenada = tupla1+ tupla2
print("Número elementos de tuplaconcatenada: ", len(tuplaconcatenada))
print("tuplaconcatenada: ", tuplaconcatenada)

# TuplaResultante = tupla * NumeroEntero,La funcionalidad "*" nos permite concatenar una tupla con ella misma un número finito de veces. 

tupla = (1,2,3,4,5,6,7,8,9,0)
print(tupla)
tuplaresultante = tupla * 4
print(tuplaresultante)



