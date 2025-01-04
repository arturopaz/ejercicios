# 3.1. Names
# Almacenar los nombres de algunos amigos en una lista llamda 'friends' luego imprimir los nombres individualmente.
# Store the names of a few of your friend in a list called 'names' then print them individually.

'''
friends = ['juan','pedro','jose','luis']

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
'''

# 3.2 Greetings
# 
'''
saludo_amigo1 = f"Hola, {friends[0].capitalize()}"
saludo_amigo2 = f"Hola, {friends[1].capitalize()}"
saludo_amigo3 = f"Hola, {friends[2].capitalize()}"
saludo_amigo4 = f"Hola, {friends[3].capitalize()}"

print(saludo_amigo1)
print(saludo_amigo2)
print(saludo_amigo3)
print(saludo_amigo4)
'''
# 3.3 Your Own List

transportation = ['auto','tren','bicicleta','avion']

print("Me gustaria viajar nuevente en", transportation[-1].title())
print(f"Montar {transportation[2].title()} es mi deporte favorito :)")
print(f"Cuando estuve en Lima me subi a un {transportation[1].title()}")
print("Cada vez que viajo al norte voy en " + transportation[0].title())