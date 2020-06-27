#
# ! Classi e Istanze : 
# ! Object = Variable = name_class(attributes)
# * Classi : ci permettono di ragruppare variabili e funzioni nei nostri programmi in maniera logica e riutilizabile.
# * Classe, spesso metaforizzata come una fabbrica di oggetti, e ciascun oggetto creato a partire da questo modello generico viene chiamato istanza.
# * Classe : non è altro che un sistema usato per modellare la realtà in modo da poter costruire e gestire oggetti più o meno complessi.

class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass

class MyClass:
    'this is my second class'
    a = 10
    def func(self):
        print(f'{self}')

    
print(MyClass.a)
print(MyClass.func('ciao mi chiamo dima'))
print(MyClass.__doc__)

# * Grazie alle classi possiamo definire le proprietà di ciascuno studente in un modello generico chiamato Classe, e da qui far derivare poi ciascun singolo individuo, assegnandole suoi attributi personali.
# * Avremmo un modello generico di Studente chiamato classe Studente, ed ogni studente creato sarà un'istanza di questo modello.
class Studente: # modello generico
                    #! variabili di istanza
    def __init__(self, nome, cognome, corso_di_studi): # aggiunta di attributi attraverso una funzione speciale, chiamata metodo, nel nostro caso è il metodo __init__ che significa inizializzatore, conosciuto anche come metodo costruttore. Il suo scopo nella fabbrica di oggetti, che è la classe, è prorpio quello di costruire gli oggetti.  Quando creiamo dei metodi all'interno della classe,  qualsiasi essi siano, tra le parentesi passiamo come primo parametro la parola self (se stesso). Self rappresenza l'istanza, quindi ciascun singolo oggetto creato dalla classe, perchè appunto rapresenta l'oggetto a cui dovranno essere associate il resto delle proprietà passate, quindi nome, cognome ecc. Self rappresenta una referenza a ciascun oggetto creato dalla classe e il metodo init inizializza ed attiva le varie proprietà di ciasun self, quindi di ciascun oggetto cui istanza
        self.nome = nome
        self.cognome = cognome                  # variabili dell'istanza
        self.corso_di_studi = corso_di_studi
        Studente.corpo_studentesco += 1 #! variabile di classe che si incremento per ogni istanza da lei creatà
    
    # aggiunta del metodo scheda personale :
    def scheda_personale(self):
        return f'Scheda Studente:\n\t Nome: {self.nome}\n\t Cognome: {self.cognome}\n\t Corso di studi: {self.corso_di_studi}\n\t Ore settimanali: {self.ore_settimanali}'
        #return f'Scheda Studente:\n\t Nome: {self.nome}\n\t Cognome: {self.cognome}\n\t Corso di studi: {self.corso_di_studi}\n\t Ore settimanali: {Studente.ore_settimanali}'
    
    ore_settimanali = 36 #! variabile di classe
    corpo_studentesco = 0  #! variabile di classe utilizzata per incrimentarne il suo valore in __init__

studente_uno = Studente('Dima', 'Tkach', 'Meccanica')
studente_due = Studente('Dragosh', 'Nistor', 'Econimia')

print('\nstudente_uno :')
print(studente_uno)
print('si tratta di un oggetto di classe Studente, oggetto di tipo Studente,\ncreato dal modello generico della classe Studente, che ha le sue proprietà e la sua allocazione di memoria\n')

print(studente_uno.scheda_personale())

# * Nesso tra classe - istanza - self : 
# * oltre a chiamare i metodi della classe sull'istanza, possiamo chiamarli sulla classe stessa, passando però come parametro il nome dell'istanza su cui vogliamo applicare il metodo.
# * Quindi di fatto questo è ciò che succede in maniera automatica qunado chiamiamo il metodo su ciascun oggetto, su ciacuna istanza, ed e prprio per questo motivo che si utilizzano i vari self, che rappresentano l'istanza passata automaticamente da Python.
print(Studente.scheda_personale(studente_due))

# ! Variabili di Istanza vs Variabili di Classe
# ! Variabili di istanza : self.variabile
# * Ciascuna istanza (oggetto) creata dalla classe (modello generico), dispone di attributi che sono propri di se stesso (self), attributi chiamati variabili di istanza, impostati tramite self, che è la parola che rappresenta la riferenza a ciascuna istanza alla classe.
# ! Variabili di Classe :
# * Sono attributi che vengono condivise da tutte le istanze della classe. 
# * Ad esempio una caratteristica comune a tutti gli studenti di un istituto potrebbe essere il numero di ore di lezioni settimanali. Quindi si potrebbe definire una variabile di classe comune a tutte le istanze senza bisogno di specificarla ogni voltà che si crea un'istanza.
# * NomeClasse.variabile_di_classe == costante di classe --> questo modo di usarla non ti permette di modificarne il valore per l'oggetto singolo, raise an exception 
# * self.variabile_di_classe == variabile di classe --> questo modo di usarla nella classe ti permette di modificarne il valore classe per l'oggetto singolo che è istanza della classe
studente_uno.ore_settimanali += 4
print(studente_uno.scheda_personale())
print(Studente.corpo_studentesco)