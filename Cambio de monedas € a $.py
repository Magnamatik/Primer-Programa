# 1 dolar = 0,92 euros
# 1 libra = 1.15 euros

print("Buenos dias, bienvenido al convertidor de monedas")

moneda_a_convertir = input("Indique que moneda quiere usted convertir \n"
                           "(A) DOLAR A EURO\n"
                           "(B) EURO A DOLAR\n"
                           "(C) LIBRA A EURO\n"
                           "(D) EURO A LIBRA\n")

if moneda_a_convertir == "A":
    dolar_euro = float(input("Cuantos Dolares quieres convertir a Euros? \n"))
    opcion1 = dolar_euro * 0.9167
    print("{} Dolares son {} Euros! ".format(dolar_euro, opcion1))

elif moneda_a_convertir == "B":
    euro_dolar = float(input("Cuantos Euros quieres convertir en Dolares? \n"))
    opcion2 = euro_dolar * 1.091
    print("{} Euros son {} Dolares!!".format(euro_dolar, opcion2))

elif moneda_a_convertir == "C":
    libra_euro = float(input("Cunatas libras quieres convertir en Euros? \n"))
    opcion3 = libra_euro * 1.149
    print("{} Libras son {} Euros!!".format(libra_euro, opcion3))

elif moneda_a_convertir == "D":
    euros_libra = float(input("Cuantos Euros quieres convertir en Libras? \n"))
    opcion4 = euros_libra * 0.8699
    print("{} Euros son {} Libras!!".format(euros_libra, opcion4))