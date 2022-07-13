import random

def run():

    #Generará un numero aleatorio entre el 1 y el 100
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 - 100: "))

    while numero_elegido != numero_aleatorio:

        if numero_elegido < numero_aleatorio:
            print("Busca uno mas grande ")
        else:
            print("Busca uno mas pequeño ")
        numero_elegido = int(input("Elige otro numero: "))

    print("¡¡Felicidades!! lo has encontrado")
        


if __name__ == '__main__':
    run()
