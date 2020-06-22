print('\nType')
rang = range(6)
print(type(rang))

dic = dict(name = 'John', age = 36)
print(type(dic))

listName = ['Dima', 'Tania', 'Massimo']

# ! instruction of flow control like : if, for, while, continue and pass
print('\ninstruction of flow control like : if, for, while, continue and pass')

# ! IF:

print('\nIF:')
import random
n = random.randrange(1, 100)
if n < 20:
   print('less than 20')
elif n > 80:
   print('more than 80')
else:
   print('between 20 and 80')

# ! FOR:
print('\nFOR:')

for x in listName:
   print(x)

print('\nFOR:')
for x in rang:
   print(x)

# * FOR con enumerate:
print('\nFOR con enumerate:')
things = ['pasta', 'frutta', 'verdura']
for cont, val in enumerate(things):
   print(cont + 1, val)

# * FOR con zip function:
print('\nFOR con zip function:')
name = ['Dima', 'Tania', 'Massimo']
age = ['31', '52', '54']
hair = ['neri', 'neri', 'neri']
for i,j,k in zip(name, hair, age):
   #print(i, 'ha i capelli', j, 'ed ha', k, 'anni')
   print(f'{i} ha i capelli {j} ed ha {k} anni')

# ! WHILE:

print('\nWHILE:')
x = 1
while x < 5:
   print(x)
   x +=1

# ! BREACK AND CONTINUE:

print('\nBREACK:')
for val in 'string':
   if val == 'i':
      break             #interrompe ed esce dal ciclo quando si verifica la condizione
   print(val)

print('\nCONTINUE:')
for val in 'string':
   if val == 'i':
      continue          #continua il ciclo saltando solo la condizione dell'IF
   print(val)

# ! RETURN:

print('\nRETURN:')
import random
n = random.randrange(1, 100)
def funzione(n):
   if n > 75:
      return 'more than 75'
   if n < 25:
      return ' less than 25'
   return 'between 25 and 75'

print(n)
print(funzione)
print(funzione(n))

# ! ASSERT:

print('\nASSERT \ninserisci due numeri uguali nella funzione per far uscire l\'eccezione dell\'assert:')
def maggiore(val1, val2):
   val_max = None
   if val1 > val2:
      val_max = val1
   if val2 > val1:
      val_max = val2
   assert val_max in (val1, val2), f'val_max = {val_max} non è in ({val1}, {val2})'
   return val_max

print(maggiore(2, 3))

# ! PASS:

print('\nPASS:')
x = 1
if x < 5:
   pass

print('\nEsempio interessante con PASS:')
for letter in 'python':
   if letter == 't':
      pass              # fai le prove inserendo continue o breack al posto di pass per vedere le differenze 
      print('passed')
   print(letter)
