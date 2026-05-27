import os
def local(name, data): #сикс севен 67 
    with open(name, 'w') as file:
        chars_written = file.write(data)
        #print(chars_written)
    #return chars_written
