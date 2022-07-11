
name = str(input("What is your name? "))

#Convierte todos los caracteres en mayusculas
print (name.upper())

#Convierte primer caracter en mayuscula
print(name.capitalize())

#Sin embargo el valor de la variable despues de la funcion no se queda guarda ya que
#si desoues decidimo imprimir solamente name éste aparecerá como se ingresó y no con 
#los cambios que se le aplicaron en la función, por ello, la menra correcta de guardarlo 
#es la siguiente:



#Convierte todos los caracteres en mayusculas
name = name.upper()

#Convierte primer caracter en mayuscula
name = name.capitalize()

#Elimina espacios basura
name = name.strip()
print(name)

#Convierto todo a minisculas
name = name.lower()
print(name)

#Cambia un caracter por otro, ejemplo 'a' por 'o'
name = name.replace('a','o')
print(name)

#Muestra la letra del indice que indicamos
name = name [0]
print(name)

#Dice la cantidad de caracteres que tiene la cadena
len(name)




#---------------------------SLICES----------------------------#
#-----------------O rebenadas

name = "Francisco"

#Imprime el caracter de la posicion que le indiquemos, en este caso 0
print(name[0])

#imprime los caracteres de la posicion 0 a 3
print(name[0:3])
#Es lo mismo que 
print(name[:3])
# O tambien: imprime de la posicion al final
print(name[3:])
#En medio o desde donde sea
print(name[1:7])


#Tambien se puede emprimir desde un incide a otro haciendo saltos, 
#en este caso de 2 en 2 y solo marcará los caracteres en los que caiga
print(name[1:7:2])
#O tambien
print(name[::])
print(name[1::2])


#O podemos imprimir la cadena al reves con
print(name[::-1])


