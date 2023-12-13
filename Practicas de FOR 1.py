numero_espacio = 0
numero_puntos = 0
numero_comas = 0
espacio = " "
coma = ","
punto = "."
texto_usuario = input("Introduzca un texto\n")

for letra in texto_usuario:
    if letra in espacio:
        numero_espacio += 1
    elif letra in coma:
        numero_comas +=1
    elif letra in punto :
        numero_puntos +=1
print("El numero de espacios es {}\n"
      "El numero de comas es {}\n"
      "El numero de puntos es {}\n".format(numero_espacio,numero_comas,numero_puntos))