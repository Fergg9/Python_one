# los sets se pueden modificar, no tienen un orden y no permiten duplicados
centroamerica_set = {'Gt', 'Hon', 'Nic', 'Cr', 'Pnm', 'Eslv' }
print(centroamerica_set)

# la podemos crear a partir de una lista
numbers = [1,2,3,1,2,3,4]
set_numbers= set(numbers)
print (set_numbers) # {1, 2, 3, 4}
# si quiero convertir este set único a una lista, lo puedo hacer:
unique_numbers = list(set_numbers)
print (unique_numbers)

#modificando sets
'''
add(): Añade un elemento.

update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

discard(): Elimina un elemento y si ya existe no lanza ningún error.

remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

clear(): Elimina todo el contenido del conjunto.
'''