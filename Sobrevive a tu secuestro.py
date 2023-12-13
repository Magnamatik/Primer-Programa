import random
import numbers
buscar_en_coche = None
probabilidad_de_sobrevivir = None
que_hacer_calabozo = None
operacion_aritmetica = None
ganzua = 0
cuchillo = 0
llaves_coche = 0

print("Sobrevive a tu secuestro!!!\n"
      "---------------------------\n"
      "\n"
      "Miercoles por la noche, te encuentras saliendo de la oficina despues de un largo\n"
      "dia de trabajo, te dirijes hacia el parking para ir hacia tu coche cuando de repente\n"
      "empiezas a oler un fuerte olor y al segundo te desmayas...\n"
      "...\n"
      "Te despiertas en un sitio muy pequeño donde casi no cabes y con mucho ruido a tu\n"
      "alrededor. Estas desorientado y no sabes que esta pasando hasta que oyes el motor \n"
      "de un coche. \n"
      "Estas en el maletero de un coche!!! \n")

maletero_coche = input("Es momento de actuar!! cual sera tu siguiente movimiento? Puede ser crucial!!\n"
                       "A - Te quedas quieto y esperas a que pase todo...\n"
                       "B - Buscas por el maletero en busca de algun objeto que te pueda ser util\n"
                       "C - Intentas saltar del coche en marcha\n")

if maletero_coche == "B":
    print("Empiezas a buscar y encuentras algo puntiagudo pero no sabes que es exactamente debido a la "
          "poca iluminacion del lugar. \n")
    coger_objecto = input("coger? (S/N)\n")

    if coger_objecto == "S":
        ganzua += 1
        print("Procedes a cojer el objecto irreconocible y te das cuenta que es una ganzua y te la guardas en los pantalones\n")
    elif coger_objecto == "N":
        ganzua += 0
        print("Te quedas quieto y callado haceindote el dormido esperando que pase todo\n")
    else:
        print()#aprender a crear un bucle/ciclo (else = volver a preguntar "coger objeto?")

elif maletero_coche == "C":     #TERMINADO!!!
    probabilidad_de_sobrevivir = random.randint(1,100)
    if probabilidad_de_sobrevivir >= 31:
        print("Entre el ruido y todo te encuentras bastante desorientado pero consigues encontrar el boton que abre \n"
              "el maletero desde dentro y saltas del coche en movimiento con tan mala suerte que te sales de la \n"
              "y te estrellas contra un arbol matandote al instante.\n")
        input("pressiona cualquier letra para salir\n")
        exit()
    elif probabilidad_de_sobrevivir <= 30:
        print("Entre el ruido y todo te encuentras bastante desorientado pero consigues encontrar el boton que abre \n"
              "el maletero desde dentro y saltas del coche en movimiento con la suerte de caer en el capo del coche \n"
              "de atras y salvandote asi de forma milagrosa!\n")
        input("pressiona cualquier letra para salir\n")
        exit(0)


print("De repente se abre el maletero y dos encapuchados te cubren la cabeza para que no puedas \n"
      "ver donde estas y te llevan a los calabozos de una casa que se encuentra en medio de la nada. Cuando llegas\n"
      "te quitan la bolsa de la cabeza y puedes ver que te encuentras en una habitacion oscura, donde practicamente\n"
      "no entra la luz y donde, lo mas seguro es que no haya habido vida en mucho tiempo ya que se encuentra llena\n"
      "de humedades y moho. En una de las paredes se oyen ruidos raros como de una persona desesperada.\n")
que_hacer_calabozo = input("A - Hablas con la persona al otro lado de la pared\n"
                           "B - Te sientas en una esquina y esperas...\n"
                           "C - Intentas escapar por la puerta\n")
if que_hacer_calabozo == "A":
    numero_random1 = random.randint(1, 167)
    numero_random2 = random.randint(1, 167)
    print("Hablando con la persona al otro lado de la pared te explica que a el tambien lo han secuestrado y \n"
          "que lleva ahi 1 semana encerrado. Te cuenta que es un enfermo de las matematicas y que si quieres \n"
          "informacion que te puede ayudar a escapar de ahi tienes que acertar el numero que el te pida.")
    operacion_aritmetica = int(input("<< Para conseguir escapar de este calabozo tendras que acertar un simple \n"
                                     "calculo matematico! Si quieres saber como escapar tendras que decirme cuanto \n"
                                     "es 867 * {} - {}?>>\n".format(numero_random1, numero_random2)))
    resultado_final = 867 * numero_random1 - numero_random2
    if operacion_aritmetica == resultado_final:
        print("<<Vaya!! Veo que se te dan bien las matematicas!!! Para salir de este calabozo tendras que \n"
              "esperar a que el secuestrador venga a traer la comida. Ahi es cuando el deja la puerta \n"
              "abierta y entra a dejar la bandeja de comida, tendras que aprovechar ese momento para dejarlo\n"
              " inconciente, pero ves con cuidado ya que es un tio de 2 metros, la unica manera de acabar \n"
              "con el es por la espalda, tendras que dejar que entre y atacarle por detras!!.>>\n"
              "\n"
              "De repente se oyen unos pasos acercandose, es uno de los secuestradores!!! Oyes como intentan abrir la puerta\n"
            "del calabozo y acto seguido entra uno de los secuestradores con una bandeja con lo que se supone que es la \n"
            "comida\n"
            "Gracias a la informacion que te dio la persona del otro lado del calabozo te escondes en una de las \n"
          "esquinas al lado de la puerta y dejas que el secuestrador entre pudiendo asi ponerte detras de el y \n"
          "dejandolo inconsciente de un golpe en la nuca!\n")

    else:
        print(
            "Vaya... Parece que no se te dan muy bien las matematicas... Has perdido tu oportunidad...\n"
            "\n"
            "De repente se oyen unos pasos acercandose, es uno de los secuestradores!!! Oyes como intentan abrir la puerta\n"
            "del calabozo y acto seguido entra uno de los secuestradores con una bandeja con lo que se supone que es la \n"
            "comida\n"
            "Debido al malestar de la comida acabas cogiendo una infeccion y, como no pagan el rescate, acabas \n"
            "muriendo en el calabozo\n")
        exit()

elif que_hacer_calabozo == "C" and ganzua == 1:
    print("Gracias a la ganzua que has encontrado antes en el maletero consigues abrir la puerta del calabozo y salir.\n")
elif que_hacer_calabozo == "C" and ganzua == 0:
    print("Te acercas a la puerta e intetas forzarla cuando de repente viene uno de los secuentradores que mide\n"
          "alrededor de 2m y te da una paliza rompiendote 3 costillas provocandote una hemoragia interna lo cual\n"
          "acabara matandote")
    exit()  # Fin posibilidad C

donde_dirigirse = input("Un vez liberado de los calabozos, cual sera tu proximo movimiento?\n"
    "A - Liberar al otro prisionero\n"
    "B - Ir a la cocina a ver si hay armas"
    "C - Ir a alguna habitacion en busca de la ventana mas cercana\n"
    "D - Ir a la salida\n")
if donde_dirigirse == "A":
        print("")  # acabar
elif donde_dirigirse == "B":
    print("te diriges a la cocina y al llegar ahi buscas en los cajones algo con lo que poder defenderte. Lo unico que\n"
          "encuentras es un cuchillo oxidado sin afilar")  # acabar
    print(coger_objecto)
    if coger_objecto == "S":
            cuchillo += 1
    if coger_objecto == "N":
            cuchillo += 0
elif donde_dirigirse == "C":
    print("te diriges a la habitacion(coger llaves)...")  # acabar
    print(coger_objecto)
    if coger_objecto == "S":
            llaves_coche += 1
    if coger_objecto == "N":
            llaves_coche += 0
    llega_secuestrador_habitacion = input("De repente viene uno de los secuestradores que haces?\n"
          "")  # acabar
elif donde_dirigirse == "D":
        print("Te diriges a la salida...(secuestrador mata)")  # acabar (muerte)
        exit()




#maletero del coche
#     3 opciones: A - No haces nada y esperas...
#                 B - Buscas en el maletero
#                 C - Intentas saltar del coche en marxa (50/50 chance)

#calabozo en sotano de casa
#     3 opciones: A - habla con compañero ¡(info x aritmetica)! 2/3 intentos?
#                             compañero da info. valiosa
#                 B - se hace el dormido y no habla
# #                             no pasa nada + no info
#                 C - intenta escapar
# #                             guardias dan paliza

#Como escapa del calabozo?
#     2 opciones: A - Con la ganzua que ha cogido del coche
#                 B - Espera a que entre el guardia
#                 C - Sale con la informacion del compañero de celda

#escapa de calabozo, donde se dirige?
#     4 opciones: A - A liberar al otro prisionero (ganzua o llave del secuestrador)
#                 B - A la cocina a por armas (consigue arma)
#                 C - A la habitacion, en busca de la ventana mas cercana (viene secuestrador)
#                             debajo de la cama (consigue llaves coche)
#                             pelea con secuestrador (muere)
#                 D - A la salida (muere por secuestrador)