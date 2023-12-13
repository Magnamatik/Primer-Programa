lista = []
que_comprar = None
salir = None
print("programa para hacer la lista de la compra!!\n")

while que_comprar != "Q" and salir != "S":
    que_comprar = input("Que desea comprar? (Q para salir)\n")
    if que_comprar in lista:
        print("{} ya esta en la lista!".format(que_comprar))


    elif que_comprar == "Q":
        salir = input("Seguro que deseas salir? [S] / [N]\n")

    else:
        anyadir = input("Seguro que quiere añadir {}? [S] / [N]\n".format(que_comprar))
        if anyadir == "S":
            lista.append(que_comprar)
            print("se ha añadido {}".format(que_comprar))

print("Tu lista de la compra es {}".format(lista))

