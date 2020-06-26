#
# ! The Files (Create, Open, close)
# * file object = open(file_name, [acces_mode], [buffering]) : a file object is created using the open function

print('\nfileopen = open("hello.txt", "w")')
fileopen = open('the_files/hello.txt', 'w')
print('name of the file:', fileopen.name)
print('closed or not:', fileopen.closed)
print('opening mode:', fileopen.mode)

# * different modes of openinga file : 

# * -> r : Opens a file for reading only. 
# * -> rb : Opens a file for reading only in binary format. 
# * -> r+ : Opens a file for both reading and writing.
# * -> rb+ : Opens a file for both reading and writing in binary format.
# * -> w : Opens a file for writing only. Overwrites the file if the file exists. If doesn't exist, creates a new file for writing
# * -> wb : Opens a file for writing only in binary form. Overwrites the file if the file exists. If doesn't exist, creates a new file for writing
# * The file pointer is placed of the beginning of the file. This is the default mode.

# * write() : 
lista = ['schumacher', 'berger', 'alonso', 'mansell']
print('\nwrite() :')
for item in lista:
    fileopen.write(item + '\n')
fileopen.close()

# * writelines() : 
print('\nwritelines() :')
fileopen = open('the_files/hello1.txt', 'r+')
sequence = ['prost\n', 'senna']
fileopen.seek(0,2)
line = fileopen.writelines(sequence)
fileopen.seek(0,0)
for index in range(4):
    line = next(fileopen)
    print(f'Line No {index} - {line}')
fileopen.close()


# * next(iteration element, default value) : Returns the next element from the iterator. If the default is provided and the iterator is exhausted, it is returned instead of increasing StopIteration.
print('\nnext() :')
fileopen = open('the_files/hello.txt', 'r')
print('name of the file :', fileopen.name)
for index in range(6):
    line = next(fileopen, 'valore di defaultn\n')
    print(f'Line No {index} - {line}')
# * qui se non definiamo un valore di default chiama l'eccezione StopIteration
#for index in range(6):
#    line = next(fileopen)
#    print(f'Line No {index} - {line}')
fileopen.close()

# * reade() : 
print('\nread() :')
fileopen = open('the_files/hello.txt', 'r+')
print('name of file :', fileopen.name)
line = fileopen.read(20)
print(f'read(20): {line}')
fileopen.close()

# * readline() : 
print('\nreadline() :')
fileopen = open('the_files/hello.txt', 'r+')
print('name of file :', fileopen.name)
line = fileopen.readline()
print(f'readline(): {line}')
line = fileopen.readline(5)
print(f'readline(5): {line}')
fileopen.close()

# * readlines() : 
print('\nreadlines() :')
fileopen = open('the_files/hello.txt', 'r+')
print('name of file :', fileopen.name)
line = fileopen.readlines()
print(f'readlines(): {line}')
line = fileopen.readlines(5)
print(f'readlines(5): {line}')
fileopen.close()

# * seek() : sets the file's current position at the offset. offset - this the position of he read/write pointer within the file.
print('\nseek() :')
fileopen = open('the_files/hello.txt', 'r+')
print('name of file :', fileopen.name)
line = fileopen.readlines()
print(f'readlines(): {line}')
fileopen.seek(25)
line = fileopen.readlines(5)
print(f'seek(25) and readlines(5): {line}')
fileopen.close()

# * tell() : returns the current position of the file read/write pointer within the file.
print('\ntell() :')
fileopen = open('the_files/hello.txt', 'r+')
print('name of file :', fileopen.name)
line = fileopen.readlines()
print(f'readlines(): {line}')
pos = fileopen.tell()
print(f'readlines() and tell(): {pos}')
fileopen.close()

# * truncate() : 
# ? da capire
print('\ntruncate() :')
fileopen = open('the_files/hello.txt', 'r+')
print('name of file :', fileopen.name)
line = fileopen.readline()
print(f'readline(): {line}')
fileopen.truncate(0)
line = fileopen.readlines()
print(f'troncate() and readlines(): {line}')
fileopen.close()

# * close() : closes the opened file. A file cannot be read or written any more. Any operation, wich requires that the file be opened will raise a ValueError after the file has been closed

# * flush() : flushes the internal buffer. Python automatically flushes the files when closing them.
# * Svuota i buffer di scrittura dello stream, se applicabile
# ? da approfondire
#fileopen.flush()

# * fileno() : 
# ? da capire 

# ! Riassunto
'''
________________________________________________________________________
fileopen = open('nome file', 'mode')
mode: w, wb, r, rb, r+, rb+
write()
writelines(iterable)
next(iterable, default)     or raise an exception
read(5)
readline()  /   readline(5)
readlines()
seek(0)
tell()
truncate()
close()
flush()
fileno()
________________________________________________________________________
'''
