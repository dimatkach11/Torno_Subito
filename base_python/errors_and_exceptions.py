print('\nSyntax Errors :')
# ! Syntax Errors and EXEPTION

a = 1
b = 0 
try:
    print('Result: ', a/b)
except ZeroDivisionError:
    print('division by zero')

try:
    d = dict(arg)
    print(d)
except TypeError:
    print('wrong type arg')
except NameError:
    print('arg not declared')

arg = 42
try:
    d = dict(arg)
    print(d)
except TypeError:
    print('wrong type arg')
except NameError:
    print('arg not declared')

arg = (('banana', 33), ('howtobasic', 2))
try:
    d = dict(arg)
    print(d)
except TypeError:
    print('wrong type arg')
except NameError:
    print('arg not declared')

# ! The raise command : 
# * il comando raise ci consente di sollevare un'eccezione 
# todo: approfondire per capire 

try:
    print('raise of the exeption')
    raise ValueError('BIngo!')
except:
    print('exception raised')
    #raise      # attiva il comando per vedere il raise == eccezione sollevata 

# ! finally

numeratore = int(input('inserisci un numeratore :'))
denominatore = int(input('inserisci un denominatore :'))
try:
    quoziente = numeratore / denominatore
except ZeroDivisionError:
    print('Denominator equal to zero')
else:
    print(f'quozionete uguale a {quoziente}')
finally:
    print('finished')