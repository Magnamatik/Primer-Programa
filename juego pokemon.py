import os
import random
import readchar
POS_X = 0
POS_Y = 1
my_position = [3, 1]
map_object = []
map_object_lenth = 5
tail_length = 0
size_hp_my_pokemon = 10
size_hp_pokemon_enemy1 = 10
size_hp_pokemon_enemy2 = 10
size_hp_pokemon_enemy3 = 10
size_hp_pokemon_enemy4 = 10
size_hp_pokemon_enemy5 = 10
HP_MY_POKEMON = 100
hp_my_pokemon_actual = HP_MY_POKEMON
HP_POKEMON_ENEMY1_INITIAL = 100
hp_pokemon_enemy1_actual = HP_POKEMON_ENEMY1_INITIAL
HP_POKEMON_ENEMY2_INITIAL = 100
hp_pokemon_enemy2_actual = HP_POKEMON_ENEMY2_INITIAL
HP_POKEMON_ENEMY3_INITIAL = 100
hp_pokemon_enemy3_actual = HP_POKEMON_ENEMY3_INITIAL
HP_POKEMON_ENEMY4_INITIAL = 100
hp_pokemon_enemy4_actual = HP_POKEMON_ENEMY4_INITIAL
HP_POKEMON_ENEMY5_INITIAL = 100
hp_pokemon_enemy5_actual = HP_POKEMON_ENEMY5_INITIAL
item = None
end_game = False
row = None
character_to_draw = None
coordinate_x = None
coordinate_y = None
is_available_to_append = None
#Creation obstacle map
obstacle_definition = '''\
####################
#               ####
#               ####
#####        #######
###     ##      ####
###   #######      #
#      ##########  #
#      #########   #
##    #####       ##
###             ####
####         #######
####      ##########
#####              #
########           #
####################\
'''
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)
#generate random objects in the map

print("¡¡SNAKE!!\n"
      "---------\n"
      "INSTRUCCIONES:\n"
      " [a] IZQUIERDA\n"
      " [d] DERECHA\n"
      " [w] ARRIBA\n"
      " [s] ABAJO\n"
      " [q] SALIR\n")


while not end_game:
# Generate random object
    while map_object_lenth >= 1:
        random_number_pos_x = random.randrange(0, MAP_WIDTH - 1)
        random_number_pos_y = random.randrange(0, MAP_HEIGHT - 1)
        random_num = (random_number_pos_x, random_number_pos_y)
        is_available_to_append = random_num not in map_object and random_num != my_position and obstacle_definition[random_num[POS_Y]][random_num[POS_X]] != "#"

        if is_available_to_append:
            map_object.append(random_num)
            map_object_lenth -= 1
# dibujo del mapa
    print("+" + "-" * (MAP_WIDTH * 3)+"¬")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            character_to_draw = "   "
            for item in map_object:

                if item[POS_X] == coordinate_x and item[POS_Y] == coordinate_y:
                    character_to_draw = " * "

                if item[POS_X] == my_position[POS_X] and item[POS_Y] == my_position[POS_Y]:
                    map_object.remove(item)

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                character_to_draw = " o "

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                character_to_draw = "###"

            if character_to_draw == "###":
                if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                    end_game = True

# deberes!!! delimitar el mapa del juego añadiendo los obstaculos (si mi posicion xoca con obstaculo = muerte)

            print("{}".format(character_to_draw), end="")

        print("|")
    print("L" + "-" * (MAP_WIDTH * 3)+"+")






#mobilidad del jugador

    direction = readchar.readchar()

    if direction == "w":
        my_position[POS_Y] -= 1
    elif direction == "s":
        my_position[POS_Y] += 1
    elif direction == "a":
        my_position[POS_X] -= 1
    elif direction == "d":
        my_position[POS_X] += 1
    elif direction == "q":
        end_game = True

    if my_position[POS_X] >= 20:
        my_position[POS_X] = 0
    elif my_position[POS_X] <= -1:
        my_position[POS_X] = 19
    elif my_position[POS_Y] >= 15:
        my_position[POS_Y] = 0
    elif my_position[POS_Y] <= -1:
        my_position[POS_Y] = 14
    os.system("cls")




#creacion combate pokemon

#combate yo y enemigo 1
print("Empieza el combate entre Pikachu y Chamrmander")
while hp_my_pokemon_actual > 0 and hp_pokemon_enemy1_actual > 0:
    #turno oponente
    turn_enemy1 = random.randint(1, 4)
    if turn_enemy1 == 1:
        hp_my_pokemon_actual -= 15
        print("Charmander uso Mordisco")
    if turn_enemy1 == 2:
        hp_my_pokemon_actual -= 20
        print("Charmander uso Lanzallamas")
    if turn_enemy1 == 3:
        hp_my_pokemon_actual -= 10
        print("Charmander uso Placaje")
    if turn_enemy1 == 4:
        hp_my_pokemon_actual -= 18
        print("Charmander uso Cola Ferrea")

    if hp_my_pokemon_actual < 0:
        hp_my_pokemon_actual = 0
    if hp_pokemon_enemy1_actual < 0:
        hp_pokemon_enemy1_actual = 0

    bars_my_pokemon = int(hp_my_pokemon_actual * size_hp_my_pokemon / HP_MY_POKEMON)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * bars_my_pokemon," " * (size_hp_my_pokemon - bars_my_pokemon),
                                                             hp_my_pokemon_actual,HP_MY_POKEMON))
    bars_pokemon_enemy1 = int(hp_pokemon_enemy1_actual * size_hp_pokemon_enemy1 / HP_POKEMON_ENEMY1_INITIAL)
    input("Charmander:  [{}{}] ({}/{})\n".format("*" * bars_pokemon_enemy1," " * (size_hp_pokemon_enemy1 - bars_pokemon_enemy1),
                                                  hp_pokemon_enemy1_actual, HP_POKEMON_ENEMY1_INITIAL))
    os.system("cls")



    # mi turno
    my_attack = None
    while my_attack != "A" or my_attack != "B" or my_attack != "C" or my_attack != "D":
        my_attack = input("Que ataque quieres usar?\n"
                          "[A] Placaje\n"
                          "[B] Cola Ferrea\n"
                          "[C] Impactrueno\n"
                          "[D] Rayo\n")
        if my_attack == "A":
            hp_pokemon_enemy1_actual -= 10
            print("Pikachu uso Placaje")
            break
        elif my_attack == "B":
            hp_pokemon_enemy1_actual -= 18
            print("Pikachu uso Cola Ferrea")
            break
        elif my_attack == "C":
            hp_pokemon_enemy1_actual -= 20
            print("Pikachu uso Impactrueno")
            break
        elif my_attack == "D":
            hp_pokemon_enemy1_actual -= 25
            print("Pikachu uso Rayo")
            break
        elif my_attack != "A" or my_attack != "B" or my_attack != "C" or my_attack != "D":
            print("Esa no es una opcion valida!!")



    if hp_my_pokemon_actual < 0:
        hp_my_pokemon_actual = 0
    if hp_pokemon_enemy1_actual < 0:
        hp_pokemon_enemy1_actual = 0

    bars_my_pokemon = int(hp_my_pokemon_actual * size_hp_my_pokemon / HP_MY_POKEMON)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * bars_my_pokemon," " * (size_hp_my_pokemon - bars_my_pokemon),
                                                             hp_my_pokemon_actual,HP_MY_POKEMON))
    bars_pokemon_enemy1 = int(hp_pokemon_enemy1_actual * size_hp_pokemon_enemy1 / HP_POKEMON_ENEMY1_INITIAL)
    input("Charmander:  [{}{}] ({}/{})\n".format("*" * bars_pokemon_enemy1," " * (size_hp_pokemon_enemy1 - bars_pokemon_enemy1),
                                                  hp_pokemon_enemy1_actual, HP_POKEMON_ENEMY1_INITIAL))


if hp_my_pokemon_actual > hp_pokemon_enemy1_actual:
    print("Pikachu ha ganado!!")
if hp_pokemon_enemy1_actual < hp_my_pokemon_actual:
    print("Charmander ha ganado!!")

#combate entre yo y enemigo 2
print("Empieza el combate entre Pikachu y Snorlax")
while hp_my_pokemon_actual > 0 and hp_pokemon_enemy2_actual > 0:
    #turno oponente
    turn_enemy2 = random.randint(1, 4)
    if turn_enemy2 == 1:
        hp_my_pokemon_actual -= 15
        print("Snorlax uso Mordisco")
    if turn_enemy2 == 2:
        hp_my_pokemon_actual -= 20
        print("Snorlax uso Avalancha")
    if turn_enemy2 == 3:
        hp_my_pokemon_actual -= 10
        print("Snorlax uso Placaje")
    if turn_enemy2 == 4:
        hp_my_pokemon_actual -= 17
        print("Snorlax uso Golpe Cuerpo")

    if hp_my_pokemon_actual < 0:
        hp_my_pokemon_actual = 0
    if hp_pokemon_enemy2_actual < 0:
        hp_pokemon_enemy2_actual = 0

    bars_my_pokemon = int(hp_my_pokemon_actual * size_hp_my_pokemon / HP_MY_POKEMON)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * bars_my_pokemon," " * (size_hp_my_pokemon - bars_my_pokemon),
                                                             hp_my_pokemon_actual,HP_MY_POKEMON))
    bars_pokemon_enemy2 = int(hp_pokemon_enemy2_actual * size_hp_pokemon_enemy2 / HP_POKEMON_ENEMY2_INITIAL)
    input("Snorlax:  [{}{}] ({}/{})\n".format("*" * bars_pokemon_enemy2," " * (size_hp_pokemon_enemy2 - bars_pokemon_enemy2),
                                                  hp_pokemon_enemy2_actual, HP_POKEMON_ENEMY1_INITIAL))
    os.system("cls")
    # mi turno
    my_attack = None
    while my_attack != "A" or my_attack != "B" or my_attack != "C" or my_attack != "D":
        my_attack = input("Que ataque quieres usar?\n"
                          "[A] Placaje\n"
                          "[B] Cola Ferrea\n"
                          "[C] Impactrueno\n"
                          "[D] Rayo\n")
        if my_attack == "A":
            hp_pokemon_enemy1_actual -= 10
            print("Pikachu uso Placaje")
            break
        elif my_attack == "B":
            hp_pokemon_enemy1_actual -= 18
            print("Pikachu uso Cola Ferrea")
            break
        elif my_attack == "C":
            hp_pokemon_enemy1_actual -= 20
            print("Pikachu uso Impactrueno")
            break
        elif my_attack == "D":
            hp_pokemon_enemy1_actual -= 25
            print("Pikachu uso Rayo")
            break
        elif my_attack != "A" or my_attack != "B" or my_attack != "C" or my_attack != "D":
            print("Esa no es una opcion valida!!")


    if hp_my_pokemon_actual < 0:
        hp_my_pokemon_actual = 0
    if hp_pokemon_enemy2_actual < 0:
        hp_pokemon_enemy2_actual = 0

    bars_my_pokemon = int(hp_my_pokemon_actual * size_hp_my_pokemon / HP_MY_POKEMON)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * bars_my_pokemon," " * (size_hp_my_pokemon - bars_my_pokemon),
                                                             hp_my_pokemon_actual,HP_MY_POKEMON))
    bars_pokemon_enemy2 = int(hp_pokemon_enemy2_actual * size_hp_pokemon_enemy2 / HP_POKEMON_ENEMY2_INITIAL)
    input("Snorlax:  [{}{}] ({}/{})\n".format("*" * bars_pokemon_enemy2," " * (size_hp_pokemon_enemy2 - bars_pokemon_enemy2),
                                                  hp_pokemon_enemy2_actual, HP_POKEMON_ENEMY2_INITIAL))

if hp_my_pokemon_actual > hp_pokemon_enemy2_actual:
    print("Pikachu ha ganado!!")
if hp_pokemon_enemy2_actual < hp_my_pokemon_actual:
    print("Snorlax ha ganado!!")

#Combate entre yo y enemigo 3
print("Empieza el combate entre Pikachu y Gyarados")
while hp_my_pokemon_actual > 0 and hp_pokemon_enemy3_actual > 0:
    #turno oponente
    turn_enemy3 = random.randint(1, 4)
    if turn_enemy3 == 1:
        hp_my_pokemon_actual -= 15
        print("Gyarados uso Mordisco")
    if turn_enemy3 == 2:
        hp_my_pokemon_actual -= 20
        print("Gyarados uso Lanzallamas")
    if turn_enemy3 == 3:
        hp_my_pokemon_actual -= 10
        print("Gyarados uso Placaje")
    if turn_enemy3 == 4:
        hp_my_pokemon_actual -= 18
        print("Gyarados uso Cola Ferrea")

    if hp_my_pokemon_actual < 0:
        hp_my_pokemon_actual = 0
    if hp_pokemon_enemy3_actual < 0:
        hp_pokemon_enemy3_actual = 0

    bars_my_pokemon = int(hp_my_pokemon_actual * size_hp_my_pokemon / HP_MY_POKEMON)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * bars_my_pokemon," " * (size_hp_my_pokemon - bars_my_pokemon),
                                                             hp_my_pokemon_actual,HP_MY_POKEMON))
    bars_pokemon_enemy3 = int(hp_pokemon_enemy3_actual * size_hp_pokemon_enemy3 / HP_POKEMON_ENEMY3_INITIAL)
    input("Gyarados:  [{}{}] ({}/{})\n".format("*" * bars_pokemon_enemy3," " * (size_hp_pokemon_enemy3 - bars_pokemon_enemy3),
                                                  hp_pokemon_enemy3_actual, HP_POKEMON_ENEMY3_INITIAL))
    os.system("cls")

    # mi turno
    my_attack = None
    while my_attack != "A" or my_attack != "B" or my_attack != "C" or my_attack != "D":
        my_attack = input("Que ataque quieres usar?\n"
                          "[A] Placaje\n"
                          "[B] Cola Ferrea\n"
                          "[C] Impactrueno\n"
                          "[D] Rayo\n")
        if my_attack == "A":
            hp_pokemon_enemy1_actual -= 10
            print("Pikachu uso Placaje")
            break
        elif my_attack == "B":
            hp_pokemon_enemy1_actual -= 18
            print("Pikachu uso Cola Ferrea")
            break
        elif my_attack == "C":
            hp_pokemon_enemy1_actual -= 20
            print("Pikachu uso Impactrueno")
            break
        elif my_attack == "D":
            hp_pokemon_enemy1_actual -= 25
            print("Pikachu uso Rayo")
            break
        elif my_attack != "A" or my_attack != "B" or my_attack != "C" or my_attack != "D":
            print("Esa no es una opcion valida!!")


    if hp_my_pokemon_actual < 0:
        hp_my_pokemon_actual = 0
    if hp_pokemon_enemy3_actual < 0:
        hp_pokemon_enemy3_actual = 0

    bars_my_pokemon = int(hp_my_pokemon_actual * size_hp_my_pokemon / HP_MY_POKEMON)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * bars_my_pokemon," " * (size_hp_my_pokemon - bars_my_pokemon),
                                                             hp_my_pokemon_actual,HP_MY_POKEMON))
    bars_pokemon_enemy3 = int(hp_pokemon_enemy3_actual * size_hp_pokemon_enemy3 / HP_POKEMON_ENEMY3_INITIAL)
    input("Gyarados:  [{}{}] ({}/{})\n".format("*" * bars_pokemon_enemy3," " * (size_hp_pokemon_enemy3 - bars_pokemon_enemy3),
                                                  hp_pokemon_enemy3_actual, HP_POKEMON_ENEMY3_INITIAL))
if hp_my_pokemon_actual > hp_pokemon_enemy3_actual:
    print("Pikachu ha ganado!!")
if hp_pokemon_enemy3_actual < hp_my_pokemon_actual:
    print("Gyarados ha ganado!!")

#Combate entre yo y enemigo 4
print("Empieza el combate entre Pikachu y Onyx")
while hp_my_pokemon_actual > 0 and hp_pokemon_enemy4_actual > 0:
    #turno oponente
    turn_enemy4 = random.randint(1, 4)
    if turn_enemy4 == 1:
        hp_my_pokemon_actual -= 15
        print("Onyx uso Mordisco")
    if turn_enemy4 == 2:
        hp_my_pokemon_actual -= 20
        print("Onyx uso Lanzarocas")
    if turn_enemy4 == 3:
        hp_my_pokemon_actual -= 10
        print("Onyx uso Placaje")
    if turn_enemy4 == 4:
        hp_my_pokemon_actual -= 18
        print("Onyx uso Cola Ferrea")

    if hp_my_pokemon_actual < 0:
        hp_my_pokemon_actual = 0
    if hp_pokemon_enemy4_actual < 0:
        hp_pokemon_enemy4_actual = 0

    bars_my_pokemon = int(hp_my_pokemon_actual * size_hp_my_pokemon / HP_MY_POKEMON)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * bars_my_pokemon," " * (size_hp_my_pokemon - bars_my_pokemon),
                                                             hp_my_pokemon_actual,HP_MY_POKEMON))
    bars_pokemon_enemy4 = int(hp_pokemon_enemy4_actual * size_hp_pokemon_enemy4 / HP_POKEMON_ENEMY4_INITIAL)
    input("Onyx:  [{}{}] ({}/{})\n".format("*" * bars_pokemon_enemy4," " * (size_hp_pokemon_enemy4 - bars_pokemon_enemy4),
                                                  hp_pokemon_enemy4_actual, HP_POKEMON_ENEMY4_INITIAL))
    os.system("cls")

# mi turno
    my_attack = None
    while my_attack != "A" or my_attack != "B" or my_attack != "C" or my_attack != "D":
        my_attack = input("Que ataque quieres usar?\n"
                          "[A] Placaje\n"
                          "[B] Cola Ferrea\n"
                          "[C] Impactrueno\n"
                          "[D] Rayo\n")
        if my_attack == "A":
            hp_pokemon_enemy1_actual -= 10
            print("Pikachu uso Placaje")
            break
        elif my_attack == "B":
            hp_pokemon_enemy1_actual -= 18
            print("Pikachu uso Cola Ferrea")
            break
        elif my_attack == "C":
            hp_pokemon_enemy1_actual -= 20
            print("Pikachu uso Impactrueno")
            break
        elif my_attack == "D":
            hp_pokemon_enemy1_actual -= 25
            print("Pikachu uso Rayo")
            break
        elif my_attack != "A" or my_attack != "B" or my_attack != "C" or my_attack != "D":
            print("Esa no es una opcion valida!!")

    if hp_my_pokemon_actual < 0:
        hp_my_pokemon_actual = 0
    if hp_pokemon_enemy4_actual < 0:
        hp_pokemon_enemy4_actual = 0

    bars_my_pokemon = int(hp_my_pokemon_actual * size_hp_my_pokemon / HP_MY_POKEMON)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * bars_my_pokemon," " * (size_hp_my_pokemon - bars_my_pokemon),
                                                             hp_my_pokemon_actual,HP_MY_POKEMON))
    bars_pokemon_enemy4 = int(hp_pokemon_enemy4_actual * size_hp_pokemon_enemy4 / HP_POKEMON_ENEMY4_INITIAL)
    input("Onyx:  [{}{}] ({}/{})\n".format("*" * bars_pokemon_enemy4," " * (size_hp_pokemon_enemy4 - bars_pokemon_enemy4),
                                                  hp_pokemon_enemy4_actual, HP_POKEMON_ENEMY4_INITIAL))
if hp_my_pokemon_actual > hp_pokemon_enemy4_actual:
    print("Pikachu ha ganado!!")
if hp_pokemon_enemy4_actual < hp_my_pokemon_actual:
    print("Onyx ha ganado!!")

#Combate entre yo y enemigo 5
print("Empieza el combate entre Pikachu y Bellsprout")
while hp_my_pokemon_actual > 0 and hp_pokemon_enemy5_actual > 0:
    #turno oponente
    turn_enemy5 = random.randint(1, 4)
    if turn_enemy5 == 1:
        hp_my_pokemon_actual -= 15
        print("Bellsprout uso Mordisco")
    if turn_enemy5 == 2:
        hp_my_pokemon_actual -= 22
        print("Bellsprout uso Giga Drenado")
    if turn_enemy5 == 3:
        hp_my_pokemon_actual -= 10
        print("Bellsprout uso Placaje")
    if turn_enemy5 == 4:
        hp_my_pokemon_actual -= 17
        print("Bellsprout uso Hoja Afilada")

    if hp_my_pokemon_actual < 0:
        hp_my_pokemon_actual = 0
    if hp_pokemon_enemy5_actual < 0:
        hp_pokemon_enemy5_actual = 0

    bars_my_pokemon = int(hp_my_pokemon_actual * size_hp_my_pokemon / HP_MY_POKEMON)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * bars_my_pokemon," " * (size_hp_my_pokemon - bars_my_pokemon),
                                                             hp_my_pokemon_actual,HP_MY_POKEMON))
    bars_pokemon_enemy5 = int(hp_pokemon_enemy5_actual * size_hp_pokemon_enemy5 / HP_POKEMON_ENEMY5_INITIAL)
    input("Bellsprout:  [{}{}] ({}/{})\n".format("*" * bars_pokemon_enemy5," " * (size_hp_pokemon_enemy5 - bars_pokemon_enemy5),
                                                  hp_pokemon_enemy5_actual, HP_POKEMON_ENEMY5_INITIAL))
    os.system("cls")

    # mi turno
    my_attack = None
    while my_attack != "A" or my_attack != "B" or my_attack != "C" or my_attack != "D":
        my_attack = input("Que ataque quieres usar?\n"
                          "[A] Placaje\n"
                          "[B] Cola Ferrea\n"
                          "[C] Impactrueno\n"
                          "[D] Rayo\n")
        if my_attack == "A":
            hp_pokemon_enemy1_actual -= 10
            print("Pikachu uso Placaje")
            break
        elif my_attack == "B":
            hp_pokemon_enemy1_actual -= 18
            print("Pikachu uso Cola Ferrea")
            break
        elif my_attack == "C":
            hp_pokemon_enemy1_actual -= 20
            print("Pikachu uso Impactrueno")
            break
        elif my_attack == "D":
            hp_pokemon_enemy1_actual -= 25
            print("Pikachu uso Rayo")
            break
        elif my_attack != "A" or my_attack != "B" or my_attack != "C" or my_attack != "D":
            print("Esa no es una opcion valida!!")

    if hp_my_pokemon_actual < 0:
        hp_my_pokemon_actual = 0
    if hp_pokemon_enemy5_actual < 0:
        hp_pokemon_enemy5_actual = 0

    bars_my_pokemon = int(hp_my_pokemon_actual * size_hp_my_pokemon / HP_MY_POKEMON)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * bars_my_pokemon," " * (size_hp_my_pokemon - bars_my_pokemon),
                                                             hp_my_pokemon_actual,HP_MY_POKEMON))
    bars_pokemon_enemy5 = int(hp_pokemon_enemy5_actual * size_hp_pokemon_enemy5 / HP_POKEMON_ENEMY5_INITIAL)
    input("Onyx:  [{}{}] ({}/{})\n".format("*" * bars_pokemon_enemy5," " * (size_hp_pokemon_enemy5 - bars_pokemon_enemy5),
                                                  hp_pokemon_enemy5_actual, HP_POKEMON_ENEMY5_INITIAL))

if hp_my_pokemon_actual > hp_pokemon_enemy5_actual:
    print("Pikachu ha ganado!!")
if hp_pokemon_enemy5_actual < hp_my_pokemon_actual:
    print("Bellsprout ha ganado!!")









