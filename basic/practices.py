
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

def run():
    contrasena = Generador_1()
    print('Tu nueva contraseña es: '+ contrasena)




def Generador_2():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = MAYUS + MINUS + NUMS + CHARS

if __name__ == "__main__":
    run()