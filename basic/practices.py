
def run():

    LIMITE = 1000
    contador = 0
    potencia_2 = 2**contador

    while potencia_2 < LIMITE:
        print(str(potencia_2))
        contador = contador +1
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()





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