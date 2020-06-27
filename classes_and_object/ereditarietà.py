# 
# ! Ereditarietà :
# * Ci consente di creare classi figlie a partire da classi genitore ereditandone cosi gli attributi ed i metodi.
# * Si possono aggiungere nuovi metodi o proprietà alle classi figlie lasciando invariatà la classe genitore.
# * L'eredetarietà permette quindi di riutilizzare del codice scritto.

# ! Genitore :
class Persona:

    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza
    
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


# ! Figli --> Nome_classe_figlia(Genitore): 
# * Aggiungo delle parenetesi al nome della classe passandole all'interno il nome della classe Genitore da cui voglio ereditare vari attributi e metodi.
# * super().__init__(variabili da gestire al genitore) : 

# ! Figlio di Persona: Studente 
class Studente(Persona):
    profilo = 'Studente:'

    def __init__(self, nome, cognome, età, residenza, corso_di_studio):
        super().__init__(nome, cognome, età, residenza) # passo le variabili che verranno gestite dalla classe genitore Persona
        self.corso_di_studio = corso_di_studio
    
    def scheda_personale(self):     # overwriting del figlio sul genitore
        scheda = f'''
        Profilo: {Studente.profilo}
        Corso di Studio: {self.corso_di_studio}'''
        return scheda + super().scheda_personale()  # richiamo il metodo scheda_personale() dal genitore attraverso super().scheda_personale()
    
    def cambio_corso(self, corso):
        self.corso_di_studio = corso
        print('Corso Aggiornato')

# ! Figlio di Persona: Insegnante
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


# ! Istanze dei Figli :
studente_uno = Studente('Dima', 'Tkach', 31, 'Massimo Grillandi 30', 'Meccanica')
#studente_uno.modifica_scheda()
print(studente_uno.scheda_personale())

insegnante_uno = Insegnante('Giuseppe', 'Schiripa', 60, 'Vasca Navale 91', ['Elettrotecnica', 'Elettronica'])
print(insegnante_uno.scheda_personale())

insegnante_uno.aggiungi_materia('Robotica')
print(insegnante_uno.scheda_personale())
studente_uno.cambio_corso('Informatica')
print(studente_uno.scheda_personale())


#print(help(Studente))