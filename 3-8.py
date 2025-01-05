# 3.8 Seeing the World
# Think of at least five places in the world you'd like to visit.

# Almacenando una lista de lugares a visitar
places = ['cusco','berlin','new york','tokio','paris','roma']

# Mostrar la lista 
print("Mis lugares favoritos a visitar son: ",places)

# Ordenando alfabeticamente sin alterar la lista original
print("La lista ordenada temporalmente: ",sorted(places))

# Mostrando la lista original
print("Mostrando mi lista original: ", places)

# Invirtiendo el orden de la lista
places.reverse()
print("Mostrando la lista invertida ", places)
places.reverse()
print("Mostrando la lista en el orden original ", places)

places.sort()
print('Mostrando la lista ordenada en orden alfabetico:', places)

places.sort(reverse=True)
print('Mostrando la lista ordenada en orden inverso alfabeticamente:', places)


