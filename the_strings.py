h = 'hello'
print(h[2])

print(h[1:3]) # stampa da 1 a 2, l'etremo destro 3 non viene compreso, il sinistro invece si

lower = 'dima'
upper = 'TKACH'
print(lower.capitalize() + upper.lower())
print(lower.islower())
print(upper.islower())

# * join
l1 = 'egg'
l2 = '123'
print(l1.join(l2)) # egg  sarà inserito in mezzo a 1, 2,  3 
print(l2.join(l1)) # 123  sarà inserito in mezzo a e, g, g

# * we can return the max and the min value of a string
print(max('strringa'))
print(min('stringa'))

# * replace
frase = 'Ciao mi chiamo Dima'
newstring = frase.replace('Dima', 'Massimo')
print(newstring)

# * isdigit() : we check if string is composed only with numbers and have a boolean output

number = '140'
newstring = number.isdigit()
print(newstring)

# * isalpha() : se ci sono solo caratteri nella stringa
char = 'stringa di solo caratteri e un numero 1'
print(char.isalpha())

# * strip() : rimuove gli spazzi bianchi in eccesso a destra e a sinistra di defoult dalla stringa
stringa = '           howtobasic is a egg war     '
print(stringa.strip(), 'ciao')

# * find() : cerca dopo la posizione specificata (opzionale) come secondo parametro, dove comincia la prima lettera della substringa ricercata se esiste, oppure restituisce -1 se non la trova o se si trova prima della posizione specificata, che di defoult parte da 0
stringa = 'Ciao mi chiamo Dima'
sub = 'chiamo'
print(stringa.find(sub, 5))
# * index() : idem a find() ma al posto di -1 ti restituisce l'errore se non trova la substringa
print(stringa.index(sub, 5))

# * swapcase() : inverte le maiuscole con le minuscole
stringa = 'CIAO mi chiamo DIMA'
print(stringa.swapcase())

# * title() : ritorna la prima lettera maiuscola : versione booleana istitle()
stringa = 'dima'
print(stringa.title())

# * zfill() : riempe a sinistra la stringa di zeri pari alla lunghezza specificata - la lughezza della stringa, nel nostro caso la stringa e lunga 19 e se noi specifichiamo zfill(24) allora avremmo 5 zeri a sinistra 
stringa = ('ciao mi chiamo Dima')
print(stringa.zfill(10))
print(stringa.zfill(24))

# * len() : lunghezza della stringa
stringa = 'ciao mi chiamo Dima'
print(len(stringa))

# * isspace() : checks wheither the string consists of whitespace
spazzi = '    '     # stringa di soli spazzi
print(spazzi.isspace())
spazzi = ''    # da notare che in questo caso darebbe False, perche non c'è niente nella stringa
print(spazzi.isspace())

# * startswith()
stringa = 'ciao mi chiamo dima ciao'
print(stringa.startswith('ciao'))

# ! maketrans() and translate() : used insieme 

intab = 'camid'
outtab = '42356'
stringa = 'ciao mi chiamo dima'
print(stringa.translate(str.maketrans(intab, outtab)))

# ! riassunto : 
'''
lower()  /  islower
upper()  /  isupper
join()
max()
min()
replace()
isdigit()
isalpha()
strip()
find()
index()
swapcase()
title()  /  istitle()
zfill()
len()
isspace()
translate() and maketrans()
'''