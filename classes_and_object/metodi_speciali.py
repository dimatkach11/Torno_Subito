# 
# ! Metodi speciali o dunder (double under scoore) : __metodo__
# * Sono dei metodi chiamati dietro le quinte.

class Studente:

    def __init__(self, nome, cognome, corso_di_studi):
        self.nome = nome
        self.cognome =cognome
        self.corso_di_studi = corso_di_studi
    
    def scheda_personale(self):
        return f'''
        Scheda Studente\n 
        Nome: {self.nome}
        Cognome: {self.cognome}
        Corso di studi: {self.corso_di_studi}
        '''
    def __add__(self, other):
        '''Uso dei dunder solo per fini didattici in maniera poco intelligente.'''
        return self.nome + ' ' + other.cognome
    
    #def __str__(self):
    #    '''Rappresentazione Leggibile -  Per il Publico'''
    #    return f'Lo Studente: {self.nome} {self.cognome} '

    def __repr__(self):
        '''Rappresentazione non Ambigua -  Per Sviluppatori'''
        return f'Studente("{self.nome}", "{self.cognome}", "{self.corso_di_studi}")'


studente_uno = Studente('Dima', 'Tkach', 'Meccanica')
studente_due = Studente('Dragosh', 'Nistor', 'Econimia')

print(studente_uno + studente_due) # ! posso usare la somma tra le classi con + perche ho definito all'interno il metodo __add__

print(studente_uno) # * se non trova __str__ prende __repr__
print(str(studente_uno)) # * se non trova __str__ prende __repr__

#print(repr(studente_uno))

# ! Maniera implicità di chiamare : attraverso il richiamo della classe che accetta come parametro l'istanza
print(Studente.__str__(studente_uno)) # * se non trova __str__ prende repr
#print(Studente.__repr__(studente_uno))

# ! Maniera esplicità : 
print(studente_uno.__str__()) # * se non trova __str__ prende repr
#print(studente_uno.__repr__())