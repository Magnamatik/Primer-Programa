print("Buenos dias, te presentamos el programa que te "
      "ayudara a decidirte a la hora de comprar un mobil!!\n")

sistema_operativo = input("Vamos a comenzar... Que sistema operativo prefieres:\n"
      "A - Android\n"
      "B - iOS\n")

if sistema_operativo == "A":
    dinero = input("Te sobra el dinero o prefieres algo mas economico?\n"
                   "A - el dinero no es un problema\n"
                   "B - prefiero algo economico\n")
    if dinero == "A":
        camara = input("Te importa la calidad de la camara?\n"
                       "A - Si\n"
                       "B - No\n")

        if camara == "A":
                print("El telefono mobil ideal para ti seria un 'Google Pixel Supercamara'!! ")
        elif camara == "B":
                print("El telefono mobil ideal para ti seria un 'Android Calidad-Precio' ")

    elif dinero == "B" :
            print("El telefono mobil ideal para ti seria un 'Android de los chinos de 100$'")

elif sistema_operativo == "B":
    dinero = input("Te sobra el dinero o prefieres algo mas economico? \n"
                   "A - el dinero no es un problema\n"
                   "B - prefiero algo mas economico\n")
    if dinero == "A":
            print("El telefono mobil ideal para ti seria un 'Iphone Ultra Pro Max'!")
    elif dinero == "B":
            print("El telefono mobil ideal para ti seria un 'Iphone de segunda mano'!!")

else:
    print("Solo las opciones A y B son posibles...")
