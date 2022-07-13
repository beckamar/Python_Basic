
numeros = [1, 2, 3, 4, 5, 6]
objetos = ["Maria", 34, 7.5, True, ]

#Para acceder a ellos es colocando el indice dentro de los corchetes
numeros[5]
objetos[3]

#Para agregar un nuevo valor a la lista: Se coloca dentro de los parentesis
numeros.append(2)
objetos.append(False)

#Mostrar las listas completas
numeros
objetos

#Eliminar un valor dentro de la lista: Se coloca el indie del elemento
numeros.pop(4)
objetos.pop(1)

#Recorrer la lista en orden
for i in numeros:
    print(i)

for i in objetos:
    print(i)

#Recorrer la lista al reves
numeros[::-1]
objetos[::-1]

#Ir de un elemento a otro, ejemplo: ir del elemento en el indice 1 al 3
numeros[1:3]
objetos[1:3]



#-------------------------- OTRAS FORMAS --------------------------

#Declar lista
my_lista = []
my_lista = list()

#Unir listas
my_lista = [1]
my_lista2 = [2,3,4]
my_lista3 = my_lista + my_lista2
my_lista3 # [1,2,3,4]

#Partir listas como slices
my_lista = [1,2,3]
my_lista[1:] # = [2,3]

#Extender una lista
my_lista = [1]
my_lista2 = [2,3,4]
my_lista.extend(my_lista2) # [1,2,3,4]

#Multiplicar listas
my_lista = ['a']
my_lista2 = my_lista * 5
my_lista2 # ['a','a','a','a','a']

#Eliminar el último elemento de la lista
my_lista = [1,2,3,4,5]
my_lista = my_lista.pop()
my_lista # [1,2,3,4]

#Ordenar lista
my_lista = [2,1,5,4,3]
my_lista = my_lista.sort()
my_lista # [1,2,3,4,5]

#Eliminar un elemento
my_lista = [1,2,3,4,5]
del my_lista[0]
my_lista # [2,3,4,5]

#Eliminar si conocemos su valor
my_lista = [1,2,3,4,5]
my_lista.remove(3)
my_lista #[1,2,4,5]

#saber qué métodos hay dentro de un elemento
dir(my_lista) # ['__add__', '__class__', '__contains__', ...

#Modificar un elemento
my_lista = [1,2,3,4,5]
my_lista[0] = 100
my_lista # [100,2,3,4,5]

#Añadir un elemento al final
my_lista = [1,2,3,4,5]
my_lista.append(6)
my_lista # [1,2,3,4,5,6]

'''
Métodos adicionales para listas
.sorted()
También ordena como sort() pero modifica la lista inicial
.clear()
Vacía la lista
.count()
Cuenta las veces que esta un elemento en lista
.index()
Indica la posición donde esta un elemento de la lista
.insert()
Inserta un elemento en una posición dada ej: lista.insert(posición,item)
.reverse()
Le da la vuelta a una lista

'''