# ! the list 
# ! LISTS
# * is an order list of heterogeneous items

lista = ['first element', 10.5, 'carbonara', 11, ['ciao', 23], 'last element']
print(lista)

# * extract the item from the list
print('\n')
print(lista[2])
print(lista[4])
print(lista[4][0])
# * to extract the last element 
print('\n')
print(lista[-1])  # estrae l'ultimo elemnto 
print(lista[len(lista) - 1])  # metodo alternativo con l'aiuto di len(lista) - 1 


# ! SLICING
# * it is one of the features of python
lista = ['first elemet', 1, 2, 3, 4, 'last element']
print(f'\nla lista presa in esame è\n{lista}')
# * extract a part of a list
print('\nextract a part of a list')
print(lista[0:4]) # l'indice a destra non è compreso, solo quello di sinistra
print(lista[0:-1]) # in questo caso l'ultimo elemento non viene considerato 
print(lista[0: len(lista)]) # cosi viene considerato anche l'ultimo elemento
# * when one of two indices is ommitted 
print('\nwhen one of two indices is ommitted')
print(lista[2:])  # mostra tutti gli elementi dal secondo indice compreso in poi 
print(lista[:2])  # mostra tutti gli elementi prima del secondo indice non compreso
print(lista[:0])  # lista vuota
print(lista[-1:]) # lista con solo l'ultimo elemento
print(lista[:-len(lista)]) # lista vuota
print(lista[:-len(lista) + 1]) # primo elemento

# * simple method to copy a list with SLICING
print('\nsimple method to copy a list')
lista_copia = lista[:]
print(lista_copia)

# * insert element in a certain position with the SLICING
menu = ['carbonara', 'amatriciana', 'cacio e pepe', 'ravioli']
print(menu)
menu[1:1] = ['montepulciano']
print(menu)

# * eliminare un elemento con SLICING
menu[1:2] = []
#menu[-4:-3] = []    # metodo equivalente a sopra ma con indici negativi
print(menu)

# ! Methods applicable to lists with dir
print('\n\n')
print(dir(menu))

# * insert() : insert an element in a desired position
print('\ninsert() :')
print(menu)
menu.insert(1, 'uova')
print(menu)

# * remove() : remove an element passed as a parameter
print('\nremove() :')
menu.remove('uova')
print(menu)

# * pop() : can extract or remove an item and can be used without an index
print('\npop() :')
menu.pop()  # without index remove the last index
print(menu)
menu.pop(1) # with index remove the index element
print(menu)

# * append() : appendi un elemento alla fine della lista, dove un elemento può essere qualunque cosa, anche un'altra lista
print('\nappend() : appendi un elemento alla fine della lista')
print(lista)
lista1 = ['dima', 31]
lista.append(lista1)
print(lista)


# * extend() : can allow us to attach directly a list with another list
# * extend() prende tutti gli elementi di un'altra lista e gli inserisce in coda alla lista desiderata dando ad ogni elemento un indice prorio a differenza di append() che prenderebbe la lista e la inserirebbe interamente in coda occupando solo un indice
print('\nextend() :')
print(menu)
menu_copy = menu[:]
whine = ['montepulciano', 'tavernello']
print(whine)
menu.extend(whine)   #osserva da qui in poi la differenza con append
print(menu, 'aggiungere una lista con extend')
menu_copy.append(whine)
print(menu_copy, 'aggiungere una lista con append')

# * count() : counts the elements of the list that are equal to the passed parameter
print('\nccount() :')
print(menu)
print(menu.count('montepulciano'))
# * count can't count the elements of a list in into another list, darà zero come risultato
print(menu_copy)
print(menu_copy.count('montepulciano'))

# * index () : returns the element or an exception if the element passed like a parameter does not exist
print('\nindex() :')
print(menu)
print(menu.index('cacio e pepe'))

# * reverse() : reverse a list and return None
print('\nreverse() :')
print(menu)
menu.reverse()
print(menu)

# * sort() : arrangees the elements of the list in alphabetical and/or numerical order if they are homogeneous and return None
print('\nsort() :')
print(menu)
menu.sort()
print(menu)

# ! LIST comprehension
# * Allow us to create a list by applying a function to the elements of another list
price = [12, 11, 13, 6]
print(price)
doubleprice = [n * 2 for n in price]
print(doubleprice)

