#
# ! Metodo di classe : @classmethod
# * Costruttore alternativo --> cls : metodo alternativo ad __init__() per istanziare oggetti. 
# * Bisogna far passare ai metodi la classe cls e non l'istanza self.
# * Per questo serve un decoratore --> @classmethod : un comando specifico per lo scopo che ci permette di alterare il comportamento dei metodi al nostro piacimento
# * @classmethod : è il decoratore che si utilizza per creare i metodi di classe. Permette di passare come parametro la classe invece che l'istanza.
# * *args : notazione specifica in Python nei casi in cui possono esserci 0 o vari parametri aggiuntivi da passare alle nostre funzioni. Utilissima sopratutto nei contesti dell'ereditarietà, dove le sottoclassi hanno dei parametri differenti della classe genitore, permettendo cosi ai nostri metodi di restare quanto più generici possibile.
# * Si possono creare dei metodi che cambiano in base alle classe che lo richiama.
# * cls : è il parametro di classe, cioè come primo parametro passiamo la classe
# * I metodi classici passano invece l'istanza come primo parametro tramite self.
# ! Metodo statico : @staticmethod
# * non si passa ne cls ne self
# * Sono funzioni che teniamo all'interno della classe, perchè hanno qualche correlazione con il contesto che stiamo modellando, ma non vi sono legati direttamente.
# * Non bisogna creare alcun oggetto per poterle richiamare.

class Persona:

    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza
    
    @classmethod
    def from_string(cls, stringa_persona, *args): # aggiunta di *args permette di richiamare tale metodo dalle classi figlie  
        nome, cognome, età, residenza = stringa_persona.split('-')
        return cls(nome, cognome, età, residenza, *args) # aggiunta di *args permette di richiamare tale metodo dalle classi figlie  

    @classmethod
    def occupazione(cls):
        #if cls.__name__== 'Studente':
        #    return 'Studente'
        #else:
        #    return 'Insegnante'
        return cls.__name__
    
    @staticmethod
    def info_prog():
        info = '''
        Nome: Persona
        Creato da: dimatkach11
        Commenti: Scritto usando python 3.8.3 64-bit
        '''
        return info

    
    def scheda_personale(self):
        sheda = f'''
        Scheda Personale:
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza} \n'''
        return sheda

    def modifica_scheda(self):
        print('''Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza''')

        scelta = input('Cosa desideri modificare ? ')
        if scelta == '1':
            self.nome = input('Nuovo Nome --> ')
        if scelta == '2':
            self.cognome = input('Nuovo Cognome --> ')
        if scelta == '3':
            self.età = int(input('Nuova Età --> '))
        if scelta == '4':
            self.residenza = input('Nuova Residenza --> ')


class Studente(Persona):
    profilo = 'Studente:'

    def __init__(self, nome, cognome, età, residenza, corso_di_studio):
        super().__init__(nome, cognome, età, residenza) 
        self.corso_di_studio = corso_di_studio
    
    def scheda_personale(self):     
        scheda = f'''
        Profilo: {Studente.profilo}
        Corso di Studio: {self.corso_di_studio}'''
        return scheda + super().scheda_personale()  
    
    def cambio_corso(self, corso):
        self.corso_di_studio = corso
        print('Corso Aggiornato')

class Insegnante(Persona):
    profilo = 'Insegnante:'

    def __init__(self, nome, cognome, età, residenza, materie=None):
        super().__init__(nome, cognome, età, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def scheda_personale(self):
        scheda = f'''
        Profilo: {Insegnante.profilo}
        Materie Insegnate: {self.materie}'''
        return scheda + super().scheda_personale()
    
    def aggiungi_materia(self, nuova):
        if nuova not in self.materie:
            self.materie.append(nuova)
        print('Materia Aggiunta')

# * bisogna istanziare una lista di persone passate come file testuale dove le persone sono separate in questo modo:
iron_man = 'Tony-Stark-40-Torre Stark'
# * Il costruttore alternativo sara in grado di gestire questa casistica prelevando i dati automaticamente da ciascuna stringa passata
persona1 = Persona.from_string(iron_man)

print(persona1.scheda_personale())

# * Se richiamo lo stesso metodo però attraverso una classe figlia, non funzionerebbe, a meno che non aggiungiamo nel costruttore alternativo from_string(cls, string_persona) *args e lo vado anche a restituire in cls()
zuch = 'Mark-Zuckerberg-33-California'
insg1 = Insegnante.from_string(iron_man, 'Ingegneria')
stud1 = Studente.from_string(zuch, 'SEO')

print(insg1.scheda_personale())
print(stud1.scheda_personale())

print(insg1.occupazione())
print(stud1.occupazione())

# * Richiamo di un metodo statico :
#  
print(Persona.info_prog())
