
def converter (type_peso, value_Dollar):

    peso = int (input("Escribe los pesos "+ type_peso + " que tienes: $" ))
    
    dollars = peso / value_Dollar
    dollars = round(dollars, 2)
    
    dollars = str(dollars)
    print("Tienes $"+dollars + " dolares") 




menu = """

Bienvenido al conversor de monedad

1. Pesos mexicanos
2. Pesos argentenios
3. Pesos colombianos

"""
opcion = int(input(menu))

if opcion == 1:
    converter("mexicanos", 20.53)
elif opcion == 2:
    converter("argentinos",127.33)
elif opcion == 3:
    converter("colombianos",4450.24)




#convertidor de dolares a pesos

#dollar = int (input("Escribe los dolares: "))
#value_Peso = .049

#pesos = dollar / value_Peso
#pesos = round(pesos,2)
#pesos = str(pesos)
#
#print("Tienes $"+ pesos + " pesos")