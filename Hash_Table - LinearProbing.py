#hashtable implemention - Linear Probing

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

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
        while True:
            try:
                if self.table[index] == item:
                    print(item, index)
                    return True
                    break
                elif item in self.table:
                    index += 1
                else:
                    return False
                    break
            except IndexError:
                index = 0
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

            
ht = HashTable(8)
ht.insert('edg')
ht.insert('ruh6')
ht.insert('stfezfc')
ht.insert('fhbc')
ht.insert('zrry')
ht.insert('r4dg')

ht.search('fhbc')
ht.search('nhfg')

ht.delete('stfezfc')
print(ht.table)

