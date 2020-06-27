#
# ! Decoratori :
# * Consentono di estendere e modificare il comportamento di classi e funzioni senza doverne alterare il codice sorgente.
# * Spesso utilizzati in Django e Flask dove le funzioni spesso hanno bisogno delle funzionalità extra.

from functools import wraps 

def caps_lock(funzione_parametro):

    @wraps(funzione_parametro) # serve per mantenere il nome della nostra funzione mia_funzione e non wrapper dopo la decorazione
    def wrapper(*args, **kwargs):
        return funzione_parametro(*args, **kwargs).upper()
    return wrapper

class Caps_lock_dc:
    def __init__(self, funzione_parametro):
        self.funzione_parametro = funzione_parametro
    
    def __call__(self, *args, **kwargs):
        return self.funzione_parametro(*args, **kwargs).upper()


def spam(funzione_parametro):

    @wraps(funzione_parametro) # serve per mantenere il nome della nostra funzione mia_funzione e non wrapper dopo la decorazione
    def wrapper(*args, **kwargs):
        print('SPAM!')
        return funzione_parametro(*args, **kwargs)
    return wrapper

@spam
#@caps_lock # <=== decoratore
@Caps_lock_dc
def mia_funzione(msg):
    return msg

#mia_funzione = caps_lock(mia_funzione) # ===> equivale a mettere il decoratore sopra la funzione da decorare
print(mia_funzione.__name__)
print(mia_funzione('eggs & bacon!'))

