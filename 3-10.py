# 3.10 Probando funciones y metodos utilizandos en el capitulo
cosas = ['salud','dinero','amor','aprendizaje','ciclismo','networking','viajar','trabajo','paz']

# Mostrando la lista original
print('Mi lista original:',cosas)

# Agregando 3 nuevos elementos a la lista
cosas.append('concentración')
cosas.append('analisis')
cosas.append('socializar')

print('Se agregando 3 nuevos elementos a la lista:', cosas)

# Insertando 1 nuevo elemento al inicio de la lista
cosas.insert(0,'descanso')
print('Se agregó 1 nuevo elemento al principio de la lista:', cosas)

# Eliminando el 4to elemento de la lista
del cosas[3]
print('Se eliminó el 4to elemento de la lista quedando así:', cosas)

# Eliminando el último elemento de la lista y mostrar cual fue y posterior a ello mostrar como quedo la lista.
elemento = cosas.pop()
print(f"Se retiró {elemento}, que fue el último elemento de la lista.")
print("La lista quedo así:", cosas)

# Eliminar el elemento 'trabajo' de la lista
cosas.remove('trabajo')
print("Se elimina el elemento 'trabajo' de la lista.")
print("La lista quedo así:", cosas)

# Ordenar alfabeticamente de manera temporal la lista
print("La lista será ordenada temporalmente de manera alfabetica:",sorted(cosas))
print("Se muestra la lista original:", cosas)

# Ordenar alfabeticamente de manera permanente
cosas.sort()
print("La lista se ordenara alfabeticamente de manera permanente:", cosas)

# Ordenar alfabeticamente inversamente de manera permanente
cosas.sort(reverse=True)
print("La lista se ordenara alfabeticamente de manera inversa permanentemente:", cosas )

# Invertir el orden de la lista de manera permanente.
cosas.reverse()
print("La lista se ha invertido su orden:", cosas)

# Mostrar la cantidad de elementos de la lista final
print("La cantidad de elementos de la lista quedo en :", len(cosas))

      

