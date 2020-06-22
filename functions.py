print('\n Default Functions or __builtins__ :')
# ! Default Functions or __builtins__ :

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