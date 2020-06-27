# 
# ! OOP : Incapsulamento e poliformismo

# ! Incapsulamento : _
# * permette di rendere "privati", in sostanza inaccessibili, attributi specifici.
# * Consente di restringere l'accesso a variabili e metodi impedendo cosi modifiche dirette a carico dei dati.
# * Si utilizza l'operatore "_"( o anche "__") come prefisso da anteporre al nome dell'attributo stesso

class Facciata:

    def __init__(self):
        # protected memeber
        self.__colore = 'verde'
    
    def colora(self):
        print(f'La facciata e di colore {self.__colore} ')
    
    def impostaColore(self, variante):
        self.__colore = variante
    
# istanza di classse
x = Facciata()
x.colora()

# modifica del colore
x.__colore = 'rosso'    # non permette di modificare la variabile, metodo privato
x.colora()

# funzione impostaColore
x.impostaColore('rosso')    # coi puoi modificare, metodo pubblico
x.colora()

# ! Poliformismo :
# * Consente di definire interfacce comuni per oggetti di classi diverse che hanno però il metodo usato nell'interfaccia in comune.

class Persiano:

    def miagola(self):
        print("Il mio persiano miagola")
    
    def graffia(self):
        print("Il mio persiano non graffia")

class Siamese:

    def miagola(self):
        print("Il mio siamese non miagola")
    
    def graffia(self):
        print("Il mio siamese graffia")

# interfaccia comune --> Poliformismo
def evento(gatto):  # <-- Interfaccia
    gatto.miagola() # <-- Metodo comune alle Classi : miagola()

# istanza oggetto
tyson = Persiano()
foreman = Siamese()

# passaggio degli oggetto all'interfaccia comune --> Poliformismo
evento(tyson)
evento(foreman)

# Come è possibile osservare, l'esempio precedente presenta due classi, "Persiano" e "Siamese".
#Ad entrambe le classi fanno riferimento due metodi omonimi, "miagola()" e "graffia()", che hanno il compito di stampare delle stringhe di testo, l'unica differenza sta nel fatto che a seconda della classe le stringhe da visualizzare a video saranno diverse.
#Per applicare il polimorfismo si è fatto però ricorso ad un'interfaccia comune, "evento()", in grado di manipolare qualsiasi oggetto, indipendentemente dalla classe in cui avviene l'istanza.
#Ecco perché quanto atteso dai metodi (nel caso specifico è stato preso in considerazione "miagola()"), viene effettivamente restituito tramite il passaggio delle istanze "tyson" e "foremean" all'interfaccia.