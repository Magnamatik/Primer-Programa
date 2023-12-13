import os
import random
import readchar
POS_X = 0
POS_Y = 1
my_position = [3, 1]
map_object = []
tail_length = 0
tail = []
tail_piece = None
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
    while len(map_object) == 0:
        random_number_pos_x = random.randrange(0, MAP_WIDTH - 1)
        random_number_pos_y = random.randrange(0, MAP_HEIGHT - 1)
        random_num = (random_number_pos_x, random_number_pos_y)
        is_available_to_append = random_num not in map_object and random_num != my_position and obstacle_definition[random_num[POS_Y]][random_num[POS_X]] != "#" and random_num != tail

        if is_available_to_append:
            map_object.append(random_num)
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
                    tail_length += 1

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    character_to_draw = " - "

                if tail_piece[POS_X] == my_position[POS_X] and tail_piece[POS_Y] == my_position[POS_Y]:
                    end_game = True

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
    if tail_piece == my_position:
        print("GAME OVER!!")





#mobilidad del jugador

    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
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



    