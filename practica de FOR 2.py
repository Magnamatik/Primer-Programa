import string

numero_mayus = 0
mayus = string.ascii_uppercase

texto_a_analizar = input("Introduzca el texto\n")
for letra in texto_a_analizar:
    if letra in mayus:
        numero_mayus += 1

print("Este texto tiene {} Mayusculas".format(numero_mayus))