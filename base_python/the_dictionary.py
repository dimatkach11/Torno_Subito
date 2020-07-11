#
# ! A dictionary is a set of objects which we can extract from a key
# * The keys in question are the one we used in the phase of the assignment

print('\n\t\t\t\t\t\tDICTIONARY\n')
keynote = dict()
keynote['tizio'] = '333-3333333'
keynote['caio'] = '444-4444444'
print(keynote)

# * copy() : 
keynote_copy = keynote.copy()

# * keys() : showing all the keys 
print('\nShowing all the keys :')
print(keynote.keys())

# * values() : showing all values
print('\nvalues() :')
print(keynote.values())

# * items() : showing all elements, keys and values
print('\nitems() :')
print(keynote.items())


# * extract a single value or raise an exception if the key dosn't exist
print('\nextract a single value : key = "caio"')
print(keynote['caio'])

# * get(key, default value) : allows us to extract a default value if the key is not present or the value of key if it is present
print('\nget("sempronio", 0) :')
print(keynote.get('sempronio', 0))
print(keynote)
print('get("tizio", 0) :')
print(keynote.get('tizio', 0))

# * setdefault(key, default value) : allows us to add the key with default value if the key specified doesn't exist
print('\nsetdefault("sempronio", "555-5555555") :')
print(keynote)
keynote.setdefault('sempronio', '555-5555555')
print(keynote)

# * if we wanna know if a key in a dictionary? we can use "in 
print('\nWe wanna khow if the key sempronio is in dictionary :')
print('sempronio' in keynote)

# * del keynote['caio] to eliminate this key from dictionary, if not exist raise an exception
print('\nEliminate key = caio :')
del keynote['caio']
print(keynote)

# * clear() : cancel all the element from the dictionary
keynote.clear()
print(keynote)

# ! Comprehension
print('\ncomprehension : ')
keynote = keynote_copy
print(keynote)
# * example, we use the dictionary comprehension to switch the keys with the value 
keynote_switch_keys_with_values = {key: value for value, key in keynote.items()}
print(keynote_switch_keys_with_values)
# * with the repeted values, in the final results, we will have one of the keys without establishing wich one
keynote['sempronio'] = '333-3333333'
print(keynote)
keynote_switch_keys_with_values = {key: value for value, key in keynote.items()}
print(keynote_switch_keys_with_values)

# ! Riassunto
'''
____________________________________________________________________________
keynote['tizio] = '333-3333333'
keynote = {'caio': '333-3333333'}
copy()
keys()
values()
items()
get(key, default value)
setdefault(key, default value) 
'tizio' in keynote  # true or false, depends if the key is exist or not
del keynote['tizio']
clear()
____________________________________________________________________________
switch the keys with the value
{key: value for value, key in keynote.items()}
with the repeted values, in the final results, 
we will have one of the keys without establishing wich one
____________________________________________________________________________
'''