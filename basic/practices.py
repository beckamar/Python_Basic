
import random
import string

def Generador_1():
    caracter = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
    contrasena = []

    while (len(contrasena) < 16):
        caracteres=random.choice(caracter)    
        contrasena.append(caracteres)

    contrasena = "".join(contrasena)
    return contrasena

def run1():
    contrasena = Generador_1()
    print('Tu nueva contraseña es: '+ contrasena)




def Generador_2():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = MAYUS + MINUS + NUMS + CHARS
    contrasena = []

    for i  in range(15):
        #choice es un funcion especial del modulo random, nos ayuda elegir un caracter al azar de la lista que hicimos
        #Ese caracter elegido se guarda dentro de la variable caracter_random 
        caracter_random = random.choice(caracteres)
        #Ahora hacemos un append para agregar el caracter elegido a la nueva lista
        contrasena.append(caracter_random)
    #Se convierte la lista en un String
    contrasena = "".join(contrasena)
    return contrasena


def run2():
    contrasena = Generador_2()
    print('Tu nueva contraseña es: '+ contrasena)


if __name__ == "__main__":
    run1()
    run2()