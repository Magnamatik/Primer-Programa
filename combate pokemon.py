import random
import os
impactrueno_total = 2
impactrueno_actual = 2
rayo_total = 4
rayo_actual = 4
placaje_total = 8
placaje_actual = 8
cola_ferrea_total = 6
cola_ferrea_actual = 6
ataque_pikachu = None
VIDA_PIKACHU_INICIAL = 86
VIDA_CHARIZARD_INICIAL = 94
tanaño_de_vida_pikachu = 10
tamaño_de_vida_charizard = 10
vida_pikachu = VIDA_PIKACHU_INICIAL
vida_charizard = VIDA_CHARIZARD_INICIAL


print("Empieza el combate entre Pikachu y Charizard\n")

while vida_pikachu > 0 and vida_charizard > 0:

    ataque_charizard = random.randint(1, 4)

    if ataque_charizard == 1:
        print("Charizard ha usado Golpe aereo\n")
        vida_pikachu -= 11
    elif ataque_charizard == 2:
        print("Charizard ha usado Lanzallamas\n")
        vida_pikachu -= 14
    elif ataque_charizard == 3:
        print("Charizard ha usado Arañazo\n")
        vida_pikachu -= 9
    elif ataque_charizard == 4:
        print("Charizard ha usado Placaje\n")
        vida_pikachu -= 7

    if vida_pikachu <0:
        vida_pikachu = 0
    if vida_charizard <0:
        vida_charizard =0

    barras_vida_pikachu = int(vida_pikachu * tanaño_de_vida_pikachu / VIDA_PIKACHU_INICIAL)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_vida_pikachu," " * (tanaño_de_vida_pikachu - barras_vida_pikachu),
                                                             vida_pikachu,VIDA_PIKACHU_INICIAL))
    barras_vida_charizard = int(vida_charizard * tamaño_de_vida_charizard / VIDA_CHARIZARD_INICIAL)
    input("Charizard:  [{}{}] ({}/{})\n".format("*" * barras_vida_charizard," " * (tamaño_de_vida_charizard - barras_vida_charizard),
                                                  vida_charizard, VIDA_CHARIZARD_INICIAL))

    os.system('cls')


    while ataque_pikachu != "A" or ataque_pikachu != "B" or ataque_pikachu != "C" or ataque_pikachu != "D":
        ataque_pikachu = input("¿Que habilidad vas a usar?\n"
                           "[A] Impactrueno {}/{}\n"
                           "[B] Rayo {}/{}\n"
                           "[C] Cola ferrea {}/{}\n"
                           "[D] Placaje {}/{}\n"
                           "[E] No Atacar\n".format(impactrueno_actual, impactrueno_total, rayo_actual, rayo_total, cola_ferrea_actual, cola_ferrea_total, placaje_actual, placaje_total))

        if ataque_pikachu == "E":
            print("No has atacado!\n")

            break
        elif ataque_pikachu != "A" and ataque_pikachu != "B" and ataque_pikachu != "C" and ataque_pikachu != "D":
            print("No es una opcion valida!\n")

        elif ataque_pikachu == "A" and impactrueno_actual > 0:
            vida_charizard -= 13
            impactrueno_actual -= 1
            print("Pikachu ha usado impactrueno\n")
            os.system('cls')
            break
        elif ataque_pikachu == "B" and rayo_actual > 0:
            vida_charizard -= 16
            rayo_actual -= 1
            print("Pikachu ha usado Rayo\n")
            os.system('cls')
            break
        elif ataque_pikachu == "C" and cola_ferrea_actual > 0:
            vida_charizard -= 11
            cola_ferrea_actual -= 1
            print("Pikachu ha usado Cola Ferrea\n")
            os.system('cls')
            break
        elif ataque_pikachu == "D" and placaje_actual > 0:
            vida_charizard -= 7
            placaje_actual -= 1
            print("Pikachu ha usado Placaje\n")
            os.system("cls")
            break
        elif impactrueno_actual == 0 or rayo_actual == 0 or cola_ferrea_actual == 0 or placaje_actual == 0:
            print("No te quedan suficientes PP!\n")

    if vida_pikachu <0:
        vida_pikachu = 0
    if vida_charizard <0:
        vida_charizard =0

    barras_vida_pikachu = int(vida_pikachu * tanaño_de_vida_pikachu / VIDA_PIKACHU_INICIAL)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_vida_pikachu," " * (tanaño_de_vida_pikachu - barras_vida_pikachu),
                                                             vida_pikachu,VIDA_PIKACHU_INICIAL))
    barras_vida_charizard = int(vida_charizard * tamaño_de_vida_charizard / VIDA_CHARIZARD_INICIAL)
    input("Charizard:  [{}{}] ({}/{})\n".format("*" * barras_vida_charizard," " * (tamaño_de_vida_charizard - barras_vida_charizard),
                                                  vida_charizard, VIDA_CHARIZARD_INICIAL))

if vida_pikachu < vida_charizard:
    print("el ganador es CHARIZARD!!")
else:
    print("El ganador el PIKACHU!!")