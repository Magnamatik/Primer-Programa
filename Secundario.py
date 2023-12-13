print("Buenos dias!!! bienvenidos un dia mas al mundo de Koper!!!")

N1 = input("Hoy tenemos con nosotros a... \n")

print("Bienvenido señor " + N1)

input("Como le ha ido hoy el dia {}. Ha sido un dia productivo??".format(N1))

print("Me alegro de oir eso!!!")

print("Esta usted aqui hoy para proporcionarnos tres numeros al azar y este programa encontrarà el numero mas bajo de todos y el mas alto!!!")

N3 = int(input("Empezemos! podria proporcionarnos un numero al azar?"))

N4 = int(input("Perfecto, gracias!!! Podria facilitarnos un segundo numero al azar?"))

N5 = int(input("Increible!!! Y para terminar, podria facilitarnos un tercer numero al azar?"))

print("Muchas gracias!!! Ya tenemos todos los datos que nos hacian falta, vamos a empezar a ordenarlos de mayor a menor...")

a = max(N3, N4, N5)
b = min(N3, N4, N5)

print("El numero mas alto de los que nos has proporcionado ha sido " + str(a))
print("Mientras que el numero mas bajo de todos es " + str(b))

print("Con esto damos por concluida nuestra emision por hoy, muchas gracias por su tiempo y hasta la proxima!!!")


