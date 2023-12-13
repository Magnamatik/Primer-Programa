
tabla_de_mutiplicar = [0,1,2,3,4,5,6,7,9,10]


numero_a_mutiplicar = int(input("De que numero quieres hacer la tabla de mutiplicar?\n"))
for numero in tabla_de_mutiplicar:
    resultado = int(numero) * numero_a_mutiplicar

    if numero % 2 == 0:
        print("{} x {} = {}".format(numero_a_mutiplicar, numero, resultado))
