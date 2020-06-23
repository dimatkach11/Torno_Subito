import sys
numeratore = int(sys.argv[1])
denominatore = int(sys.argv[2])
try:
    quoziente = numeratore / denominatore
except ZeroDivisionError:
    print('except')
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])
else:
    print(f'quozionete uguale a {quoziente}')
finally:
    print('finished')

# ! Per far funzionare lo script devi farlo eseguire da terminale passando due valori degli argomenti argv
# * cosi :      python3 sys_exception.py 10 2 
# * dove 10 e 2 sono i paramtri scelti come esempio respittivamente per argv[1] e argv[2]