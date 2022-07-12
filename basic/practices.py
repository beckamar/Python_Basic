
#for ---> de un rango a otro

for contador in range(0, 100):
    print(contador)


#for ----> Con String
def runFor():
    nombre = input("Escribe tu nombre: ")
    for letra in nombre:
        print(letra)

    #2
    frase = input("Escriba una frase: ")
    for caracter in frase:
        print(caracter.upper())


#While
def runWhile():

    LIMITE = 1000
    contador = 0
    potencia_2 = 2**contador

    while potencia_2 < LIMITE:
        print(str(potencia_2))
        contador +=1
        potencia_2 = 2**contador


if __name__ == "__main__":
    runWhile()
    runFor()





#def run(num, rept):
#    if num <= rept:
#        cont = num
#        print(str(2 ** cont) )
#        run(num+1, rept)
#    else:
#        print("Fin!")
#
#if __name__ == "__main__":
#    repeticiones = int(input("Cuantas potencias: "))
#    run(0, repeticiones)