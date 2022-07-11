
#convertir de pesos a dolares 

peso = int (input("Escribe los pesos: "))
value_Dollar = 20.53

dollars = peso / value_Dollar
dollars = round(dollars, 2)

dollars = str(dollars)
print("Tienes $"+dollars + " dolares") 


#convertidor de dolares a pesos

dollar = int (input("Escribe los dolares: "))
value_Peso = .049

pesos = dollar / value_Peso
pesos = round(pesos,2)
pesos = str(pesos)

print("Tienes $"+ pesos + " pesos")