print('\n Default Functions or __builtins__ :')
# ! Functions:

print('\nFunctions\nfattoriale di 5:')
def fact(n):
   '''
   This function return the factorial.      
   n is the parameter.
   '''
   if n < 2:
      return 1
   return n * fact(n - 1)

print(fact(5))    # ? 5 * 4 * 3 * 2 * 1 
print(help(fact)) 

# * multiple return:
print('\nmultiple return:')
def throw_egg():
   return 'throw', 'egg'

t, e = throw_egg()
print(t)
print(e)

# * the same option is available with list and tuple:
print('\nthe same option is available with list and tuple:')
list = [1,2]
elem1, elem2 = list
tupla = ('a', 'b', 'c')
elem3, elem4, elem5 = tupla
print(elem1)
print(elem2)
print(elem3)
print(elem4)
print(elem5)

# * Advanced tecnique for passing arguments
# * Happen when we need to pass in a function a list of parameters not defined beforhand
# * Python gives us two possibilities that we can both use in the same function:
# * *parameters: trasform a list of parameters (without name and length) in a tuple
# * **keyword: trasform a list of parameters (with name and arbitrary length) in a dictionary

print('\nAdvanced tecnique for passing arguments:')
print('\nEsempio tupla')
def spesa1(*cosa):   # bisogna aggiungere un * davanti al parametro cosa
   print(type(cosa))
   for x in cosa:
      print(x)
spesa1('pasta', 'mandorle', 'farina')

print('\nEsempio dizionario')
def spesa2(**cosa): # bisogna aggiungere due ** davanti al parametro cosa
   print(type(cosa))
   for x,y in cosa.items():
      print(x, y)
spesa2(first = 'pasta', second = 'mandorle', third = 'farina')

# * In Python a function is at all an object too
# * We can assign the function an a variable 

print('\nFunction is at all an object too:')
def stamp(thing):
   print(thing)

f = stamp
f('hello')

# ! Default Functions or __builtins__ without import it becouse this module is load by python:
 
print('\n __builtins__ functions: dir(__builtins__)')
print(dir(__builtins__))

# * Many default objects are an exeption, other are real functions, others are classes.
# * Most use and relevant ones are:

print('\nMost used and relevant builtins function:')

print(max(1,2,3))
print(min(1,2,3))

print(sum((1,2),-6))  # * prende solo due argomenti, un iterabile e un valore di start che di default = 0 se omesso

print(pow(2,5))
print(pow(2, 100, 37))     # ?
print(pow(2, 100) % 37)    # ?

print(abs(-5))  
print(abs(3 + 4j))   # * calcola la norma

print(round(4.2111, 0))
print(round(4.2111, 1))
print(round(4.2111, 2))

print(all([n > 10 for n in (5, 15, 25, 35, 45)]))
print(all([n > 10 for n in (50, 15, 25, 35, 45)]))

print(any([n > 10 for n in (5, 15, 25, 35, 45)]))
print(any([n > 10 for n in (5, 1, 2, 3, 4)]))

print(chr(65))
print(ord('A'))

# ! MAP, ZIP AND FILTER

# * MAP : 
# * execute the function passed as the first parameter, using the values taken from the next iterable parameters and returns an iterable
def add(a,b,c):
   return a+b+c
for n in map(add, [1,2,4,5], [5,6,3], [10,20]): # fa 1+5+6 ed 2+6+20
   print(n)

# * ZIP :
# * recives a list of iterabiles and extracts a value from each one and insert in a tuple  
for x in zip([1,2,3,4,5], 'hello', 'ciao'):
   print(x)

# * FILTER :
# * applies the function to the elements of the iterable, returning only those for witch the function assumes True value
def major(n):
   return n > 23
for n in filter(major, [10,30,50]):
   print(n)