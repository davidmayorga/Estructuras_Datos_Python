# Diccionario
print("------------Ejercicio1------------")
# Ejercicios
## Los ejercicios con diccionarios los hemos dividido en dos grupos diferentes. El primer grupo de ejercicios consiste en la manipulación de los diccionarios y el segundo grupo consiste en el aprendizaje de los métodos propios de los tipos de datos diccionario.
#### Manipulacion:Esto nos permitira acceder a los elementos del diccionario con el siguiente código:
diassemanaingles = {"Lunes " : "Monday",
                    "Martes": "Tuesday",
                    "Miercoles": "Wednesday", 
                    "Jueves":"Thursday",
                    "Viernes":"Friday"}
print(diassemanaingles["Lunes"])
print(diassemanaingles["Miercoles"])
print (diassemanaingles["Viernes"])


print("------------Ejercicio2------------")

## El siguiente ejercicio consiste en añadir elementos al diccionario, eliminar elementos del diccionario y en modifica el valor de los elementos del diccionario 

## Laforma de añadir un elemento al diccionario es la siguiente:
### Diccionario[NuevaClave] = NuevoValor

## La forma de modificar el valor de un elemento del diccionario es la siguiente:
### Diccionario[ClaveQueSeVaAModificar]= NuevoValor

## La forma de eliminar un elemento del diccionario es la siguiente:
### DEL Diccionario[ClaveElementosABorrar]

# En el siguiente ejercicio se añadira Sabado y Domingo, modificando y borrando algun elemento


diassemanaingles = {"Lunes " : "Monday",
                    "Martes": "Tuesday",
                    "Miercoles": "Wednesday", 
                    "Jueves":"Thursday",
                    "Viernes":"Friday"}
print(diassemanaingles)
diassemanaingles["Sabado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)
del diassemanaingles["Lunes"] 
print(diassemanaingles)
del diassemanaingles["Lunes"]
print(diassemanaingles)

print("---------Ejercicio3---------")

##  Es posible utilizar las funciones len, max y min con los diccionarios. La primera devolverá el número de elementos que contiene el diccionario; la segunda, el elemento con el valor mayor y la tercera, el elemento con el valor menor. El valor mayor y el valor menor serán devueltos siempre que pueda calcularse dependiendo de los elementos que componen el diccionario. Veámoslo en un ejercicio. El código fuente es el siguiente:
diassemanaingles = {"Lunes" : "Monday",
                    "Martes" : "Tuesday",
                    "Miercoles" : "Wednesday",
                    "Jueves":"Thursday",
                    "Viernes" : "Friday"}

print("Número de elementos del diccionario: ",len(diassemanaingles))
print("Elemento mayor del diccionario: ",max(diassemanaingles))
print("Elemento menor del diccionario: ",min(diassemanaingles))

print("---------Ejercicio4---------")

# MÉTODOS PROPIOS
## El tipode dato diccionario en python posee una serie de funciones que nos permiten manipular los diccionarios realizando operaciones complejas de forma sencilla y con una simple instrucción. El formato de uso de la gran mayoría de las funciones siguientes :
### Diccionario.NombreFuncion(Parámetros)

## Veamos en detalle cada una de las partes:

## Diccionario: diccionario que ejecuta la función.
## NombreFuncion: nombre de la función que se quiere ejecutar.
## Parámetros: no todas las funciones tienen parámetros para ejecutarse, esta parte es dependiente de la función que se quiere ejecutar.
## La funciones de listas que pone a nuestra disposición Python son las siguientes:
## copy: realiza una copia exacta del diccionario en uno nuevo.
## ⚫ Valor devuelto: diccionario copiado.
## • Parámetros: no tiene.
## pop: obtiene el valor de la clave pasada como parámetro y además elimina el elemento del diccionario.
## • Valor devuelto: valor del elemento o error en caso de no encontrar la clave en el diccionario.
## • Parámetros: clave a buscar en el diccionario.
## popitem: obtiene un elemento aleatorio del diccionario y lo elimina del mismo.
## ⚫ Valor devuelto: elemento del diccionario y en caso de que no tenga elementos el diccionario da un error.
## ⚫ Parámetros: no tiene.
## get: obtiene el valor de la clave pasada como parámetro.
##• Valor devuelto: devolverá el valor del elemento en caso de existir dicha clave y en caso de no existir devolverá "None". Existe la posibilidad de especificar mediante un segundo parámetro un valor diferente a "None" como retorno en caso de no existir la clave.
## • Parámetros: tiene dos parámetros, el primero es clave del elemento a buscar y el segundo es opcional y es el valor que se quiere retornar en caso de no existir dicha clave en el diccionario. obligatorio y es la
## update: realiza una actualización del diccionario utilizando otro diccionario, Aquellos elementos del diccionario que se utilizan para actualizar el principal sustituirán los existentes en el mismo y aquellos elementos que no existan serán añadidos al diccionario como nuevos elementos.
#Valor devuelto: nuevo diccionario.
# Parámetros: diccionario.
#setdefault: intenta insertar un elemento (clave y valor) en el diccionario. En caso de no existir dicho elemento, la función inserta y devuelve el valor del elemento y en caso de existir, lo único que hace es devolver el valor actual.
#Valor devuelto: diccionario resultante.
# Parámetros: dos parámetros que son la clave y valor. Es posible no especificar el valor y por defecto se insertará el valor None como valor del elemento.
#clear: elimina todos los elementos del diccionario.
#Valor devuelto: diccionario vacío.
#Parámetros: no tiene.
#items: devuelve un objeto iterable (que puede utilizarse en bucles. Lo veremos en próximos capítulos) compuesto por todos los elementos del diccionario.
#Valor devuelto: objeto iterable compuesto por los elementos del diccionario.
###Parámetros: no tiene.
### keys: devuelve un objeto iterable (que puede utilizarse en bucles. Lo veremos en próximos capítulos) compuesto por todas las claves del diccionario.
###Valor devuelto: objeto iterable compuesto por las claves del diccionario.
###Parámetros: no tiene.
#values: devuelve un objeto iterable (que puede utilizarse en bucles. Lo veremos en próximos capítulos) compuesto por todos los valores del diccionario.
### Valor devuelto: objeto iterable compuesto por los valores del diccionario.
### Parámetros: no tiene.
## A continuación vamos a realizar un ejercicio para aprender a utilizar ambas funciones de los diccionarios.

print("-------Ejercicio 3 -------")
diassemanaingles={"Lunes" : "Monday",
                 "Martes" : "Tuesday",
                 "Jueves": "Thursday",
                 "Miercoles": "Wednesday", 
                "Viernes": "Friday"} 
print("Diccionario original: ", diassemanaingles)
diccionariocopia = diassemanaingles.copy()
print("Diccionario copy: ",diccionariocopia)
print("Valor del Lunes (pop): ", diassemanaingles.pop("Lunes"))
print("Diccionario después del pop: ",diassemanaingles)
print("Elemento al azar con popitem: ", diassemanaingles.popitem())
print("Diccionario después del popitem: ", diassemanaingles)
print("Valor del Martes (get): ",diassemanaingles.get("Martes")) 
print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes"))
print("Valor del Lunes (get) (no existe): ", diassemanaingles.get("Lunes", "No existe"))
diassemanaingles.update({"Lunes":"MondayNUEVO", "Martes":"TuesdayNUEVO"})
print("Diccionario después del update: ",diassemanaingles)
print("setdefault del Sábado: ",diassemanaingles.setdefault("Sabado", "Saturday"))
print("Diccionario después del setdefault (nuevo elemento): ",diassemanaingles) 
print("setdefault del Lunes: ",diassemanaingles.setdefault ("Lunes", "Lunes"))
print("Diccionario después del setdefault (elemento existente): ",diassemanaingles)

print("Elemento iterable (items): ",diassemanaingles.items())
print("Elemento iterable (claves): ",diassemanaingles.keys()) 
print("Elemento iterable (valores): ",diassemanaingles.values())
print("Diccionario después del clear: ",diassemanaingles.clear())