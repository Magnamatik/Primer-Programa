

print("Bienvenidos al Ultimate LoL Test!! Aqui pondreis a "
      "prueba vuestro fanatismo del LoL!!!\n")
print("Este test consiste en 10 preguntas de amplia diversidad "
      "todo relacionado con el juego. Crees que sabes del LoL?? Adelante!!! Demuestralo!!\n")

puntuacion = 0

Pregunta1 = input("¿En que año salio el juego mundialmente conocido como League of Legends?\n"
                  "A - 2011\n"
                  "B - 2009\n"
                  "C - 2010\n")

if Pregunta1 == "A":
    puntuacion +=0
if Pregunta1 == "B":
    puntuacion +=1
if Pregunta1 == "C":
    puntuacion +=0

Pregunta2 = input("¿Cual de estas habilidades es el nombre la ultimate de Ekko?\n"
                      "A - Salto de Fase\n"
                      "B - Convergencia Paralela\n"
                      "C - Fisura Temporal\n")

if Pregunta2 == "A":
        puntuacion += 0
if Pregunta2 == "B":
        puntuacion += 0
if Pregunta2 == "C":
        puntuacion += 1

Pregunta3 = input("¿Quien fue el conocido midlaner del equipo ruso Moscow5?\n"
                  "A - Reginald\n"
                  "B - Alex Ich\n"
                  "C - Froggen\n")

if Pregunta3 == "A":
    puntuacion +=0
if Pregunta3 == "B":
    puntuacion +=1
if Pregunta3 == "C":
    puntuacion +=0

Pregunta4 = input("¿Cuanto dinero da una de las cinco placas que tienen las primeras torres\n"
                  "A - 125\n"
                  "B - 150\n"
                  "C - 100\n")

if Pregunta4 == "A":
    puntuacion +=1
if Pregunta4 == "B":
    puntuacion +=0
if Pregunta4 == "C":
    puntuacion +=0

Pregunta5 = input("¿De que faccion forma parte el personaje RAMMUS\n"
                  "A - Noxus\n"
                  "B - Piltover\n"
                  "C - Shurima\n")

if Pregunta5 == "A":
    puntuacion +=0
if Pregunta5 == "B":
    puntuacion +=0
if Pregunta5 == "C":
    puntuacion +=1

Pregunta6 = input("¿Cual de estos personajes utiliza la FURIA?\n"
                  "A - Gnar\n"
                  "B - Tryndamere\n"
                  "C - Lee Sin\n")

if Pregunta6 == "A":
    puntuacion +=1
if Pregunta6 == "B":
    puntuacion +=0
if Pregunta6 == "C":
    puntuacion +=0

Pregunta7 = input("¿En que año se proclamo vencedor de los Worlds el equipo llamado Taipei Assassins (TPA)?\n"
                  "A - 2014\n"
                  "B - 2013\n"
                  "C - 2012\n")

if Pregunta7 == "A":
    puntuacion +=0
if Pregunta7 == "B":
    puntuacion +=0
if Pregunta7 == "C":
    puntuacion +=1

Pregunta8 = input("¿Con que personaje se realizo el movimiento conocido como insec?\n"
                  "A - Kassadin\n"
                  "B - Lee sin\n"
                  "C - Nunu\n")

if Pregunta8 == "A":
    puntuacion +=0
if Pregunta8 == "B":
    puntuacion +=1
if Pregunta8 == "C":
    puntuacion +=0

Pregunta9 = input("¿Como se llamaba el famoso jugador Español xPeke?\n"
                  "A - Enrique Cedeño\n"
                  "B - Carlos Rodriguez\n"
                  "C - Alvar Martin \n")

if Pregunta9 == "A":
    puntuacion +=1
if Pregunta9 == "B":
    puntuacion +=0
if Pregunta9 == "C":
    puntuacion +=0

Pregunta10 = input("¿Cuantos dragones hacen falta matar para conseguir el alma de dragon?\n"
                  "A - 5\n"
                  "B - 3\n"
                  "C - 4\n")

if Pregunta10 == "A":
    puntuacion +=0
if Pregunta10 == "B":
    puntuacion +=0
if Pregunta10 == "C":
    puntuacion +=1


if puntuacion == 10:
    print("Felicidades!!! estas hecho un crack!!! Te lo sabes todo sobre el LoL!!! ")

elif puntuacion >=5:
    print("Se nota que sabes del juego pero estas algo oxidado... ")

elif puntuacion <5:
    print("Hmmm no habra sido suerte no? ")

elif puntuacion ==0:
    print("A quien intentas engañar? se nota que es tu primer dia ")
#<
#>