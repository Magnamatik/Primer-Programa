import os
lista = []
print("bienvenido al creador de listas\n")

numero_a_aniadir = int(input("Que numero quieres añadir a la lista?\n"))
lista.append(numero_a_aniadir)


while input("Desea añadir otro numero? (S/N)\n") == "S":
    numero_a_aniadir = int(input("Que numeros quieres añadir a la lista?\n"))
    lista.append(numero_a_aniadir)
    os.system("cls")

print(lista)

print("el numero mas alto de la lista es :" + str(max(lista)))
print("el numero mas bajo de la lista es :" + str(min(lista)))


'''
ALTERNATIVA ESTANDARD:
print("bienvenido al creador de listas\n")
numero_a_aniadir = int(input("Introduzca los numeros separados por coma: \n"))  #1,2,3,4,5,6,7,8,90,3,2,545,
lista = numero_a_aniadir.split(",")
lista_final = []

for numero in lista:
    lista final.append(int(numero)) # asi creamos otra lista donde todos los numero de la primera lista pasaran a la segunda lista pero en forma "int"




ALTERNATIVA PRO: (simplificado 100%)
print("bienvenido al creador de listas\n")
numero_a_aniadir = int(input("Introduzca los numeros separados por coma: \n"))  #1,2,3,4,5,6,7,8,90,3,2,545,
lista = numero_a_aniadir.split(",")

lista = [int(numero) for numero in numero_a_aniadir] #esto hara que cada item de la lista creada pase a convertirse en "int"
'''