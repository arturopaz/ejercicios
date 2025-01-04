guests = ['jose paz','susana puerta','pedro puerta','marlon sisniegas']

print(f"Mis invitados son: {guests}" )



no_asiste = guests.pop(2).title()
print(f"Al parecer {no_asiste} no podrá asistir a la cena. :(")

nuevo_invitado = 'juan perez'

guests.insert(2,nuevo_invitado)
message = "No faltes!!"

print("A los nuevos invitados los esperamos a la cena del día 05-01-2025·")
print(f"Hola {guests[0].title()}, {message}")
print(f"Hola {guests[1].title()}, {message}")
print(f"Hola {guests[2].title()}, {message}")
print(f"Hola {guests[3].title()}, {message}")

print("Tenemos 3 espacios disponibles para invitados")

invitado1 = "benito Juarez" 
invitado2 = "Pedro Picapiedra"
invitado3 = "pablo marmol"

guests.insert(0,invitado1)
guests.insert(2,invitado2)
guests.append(invitado3)

print("\n A los nuevos invitados los esperamos:\n\n")

print(f"Hola {guests[0].title()}, {message}")
print(f"Hola {guests[1].title()}, {message}")
print(f"Hola {guests[2].title()}, {message}")
print(f"Hola {guests[3].title()}, {message}")
print(f"Hola {guests[4].title()}, {message}")
print(f"Hola {guests[5].title()}, {message}")
print(f"Hola {guests[6].title()}, {message}")