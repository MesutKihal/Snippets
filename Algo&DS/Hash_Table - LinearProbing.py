#hashtable implemention - Linear Probing

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def __repr__(self):
        hash_table_scheme = '|'+'Index'.rjust(6)+ '|'.center(4) +'Item'.rjust(6)+'\n'+'|'+'-'*7+'|'+'-'*30+'\n'
        i = 0
        for item in self.table:
            hash_table_scheme += '|'+str(i).rjust(4) + '|'.center(8)+str(item)+'\n'
            i += 1
        return hash_table_scheme

    def hash_(self, item):
        temp = str(item)
        count = 0
        for char in temp:
            count += ord(char.upper()) - ord("A")
        return (count//len(temp))%self.size
    
    def insert(self, item):
        index = self.hash_(item)
        while True:
            try:
                if self.table[index] == None:
                    self.table[index] = item
                    break
                elif None in self.table:
                    index += 1
                else:
                    break
                    
            except IndexError:
                index = 0
    def search(self, item):
        index = self.hash_(item)
        message = False
        while True:
            try:
                if self.table[index] == item:
                    message = True
                    break
                elif item in self.table:
                    index += 1
                else:
                    message = False
                    break
            except IndexError:
                index = 0
        return message
    def delete(self, item):
        index = self.hash_(item)
        while True:
            try:
                if self.table[index] == item:
                    self.table[index] = None
                    break
                elif None in self.table:
                    index += 1
                else:
                    break
            except IndexError:
                index = 0

            
ht = HashTable(9)
ht.insert('madara')
ht.insert('sasori')
ht.insert('konohamaru')
ht.insert('minato')
ht.insert('shisui')
ht.insert('sai')
ht.insert('itachi')
ht.insert('kurama')
ht.insert('kakashi')

print(ht.search('sasori'))
print(ht.search('hiruzen'))

ht.delete('kakashi')
print(ht)

