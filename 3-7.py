# Shrinking Guest List

guests = ['jose paz','susana puerta','pedro puerta','marlon sisniegas','pablo marmol']

print("Atención: Solo podremos invitar a 2 personas a la cena.\n")

invitado1 = guests.pop()
print(f"Lo sentimos {invitado1} por no poder invitarte a la cena.")
invitado2 = guests.pop()
print(f"Lo sentimos {invitado2} por no poder invitarte a la cena.")
invitado3 = guests.pop()
print(f"Lo sentimos {invitado3} por no poder invitarte a la cena.")

print("Saludo a los invitados que quedaron:")
print(f"{guests[0].title()}, felicidades aun estas invitado a la cena.")
print(f"{guests[1].title()}, felicidades aun estas invitado a la cena.")

print("Eliminando invitados de la lista...")
del guests[0]
del guests[0]

print("La lista de invitados final es: ", guests)