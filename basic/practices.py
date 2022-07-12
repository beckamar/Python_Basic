
#for ---> de un rango a otro

from unittest import main


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


#break
def runBreak():
    for i in range(100):
        print(i)
        if i == 58:
            break
        #2
    text = input("Escribe un texto: ")
    for i in text:
        if i == 'o':
            break
        print (i)


#continue
def runContinue():
    for i in range(1,100):
        if i % 2 != 0:
            continue
        print(i)


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
    #runWhile()
    #runFor()
    runContinue()
    runBreak()




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