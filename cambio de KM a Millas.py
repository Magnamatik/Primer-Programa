unidad_de_medida = input("Que unidad de medida quieres convertir?\n"
                      "(K) - Kilometros \n"
                      "(M) - Millas \n")


if unidad_de_medida == "K":
    kilometros = float(input("Cuantos Kilometros quieres convertir en Millas? \n"))
    K = kilometros * 0.6214
    print("{} kilometros son {} millas \n".format(kilometros, K))

if unidad_de_medida == "M":
    millas = float(input("Cunatas Millas quieres convertir en Kilometros? \n"))
    M = millas / 0.6214
    print("{} millas son {} kilometros \n".format(millas,M))
