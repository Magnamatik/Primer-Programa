import random


Numero_a_adivinar = random.randint(1,10)


Intento1 = int(input("Si adivinas el numero de la suerte ganaras esta edicion,"
                    "por favor, diganos un numero del 1 al 10 \n"))

if Intento1 == Numero_a_adivinar:
    print("Enorabuena!!! ha ganado usted esta edicion!! ")

if Intento1 != Numero_a_adivinar:
    print("Vaya que mala suerte!!! ")
    Intento2 = int(input("Vuelve a intentarlo!!\n"))
    if Intento2 == Numero_a_adivinar:
        print("Felicidades esta vez has acertado!!!")

    if Intento2 != Numero_a_adivinar:
        print("Casi!!! sigue probando!!!")
        Intento3 = int(input("Ultima oportunidad!!!\n"))

        if Intento3 == Numero_a_adivinar:
            print("Ahora si!!!! ese es!!!")
        if Intento3 != Numero_a_adivinar:
            print("vaya... no ha habido suerte... Suerte la proxima!!")




print("el numero correcto era {}".format(Numero_a_adivinar))
#<
#>