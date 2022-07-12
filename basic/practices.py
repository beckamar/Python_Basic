#(n-1)! + 1 es múltiplo de n

def fac(number):
    
    factorial = 1
    for i in range(1, number):
        factorial *= i
    
    factorial += 1
    return factorial


def determine():

    number = int(input("Escribe un numero: "))
    if number > 1:
      if fac(number) % (number):
          print("No es primo")
      else:
          print("Es primo")
    else:
        print()



if __name__ == "__main__":
    determine()





#def run():
#    number = int(input('Escribe un numero: '))
#    print('Es primo'if (isPrime(number)) else'No es primo')
#
#def isPrime(num):
#    return ((factorial(num - 1) + 1) % num) == 0ifnum > 1else False
#
#def factorial(num):
#    return1ifnum <= 1else (num * factorial(num - 1))
#
#if __name__ == '__main__':
#    run()