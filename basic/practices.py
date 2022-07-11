
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

#Elimina espacios 
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