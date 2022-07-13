#Las listas son dinamicas pero necesitan muchan memeoria
#Las tuplas son estaticas y no se le pueden borrar o agregar elementos.
#Si recorreremos una lista con el ciclo for será mucho más rapido con las Tuplas

#LAS TUPLAS SON INMUTABLES


#Declarar tupla
mi_tupla= ()
mi_tupla = (1, 2, 3, 4, 5, 6)

#Generar una tupla de 1 solo valor
#La , es obligatoria.
mi_tupla = (1,)

#Acceder a un índice de la tupla
mi_tupla = (1,2,3)
mi_tupla[0] #1
mi_tupla[1] #2
mi_tupla[2] #3

#mi_tupla = (1,2,3)
mi_tupla = (1,2,3)
mi_otra_tupla = (4,5,6)
mi_tupla =+ mi_otra_tupla

#Métodos para trabajar con tuplas
#Usando el ejemplo:
mi_tupla = (1,1,1,2,2,3)

'''
Encontraremos los siguientes métodos:

mi_tupla.count(1)
Devolverá 3, ya que el número 1 aparece 3 veces en la tupla.
mi_tupla.index(3)
Devolverá 5, índice de la primera instancia donde se encuentra un elemento.
mi_tupla.index(1)
Devolverá 0
mi_tupla.index(2)
Devolverá 3.
'''
