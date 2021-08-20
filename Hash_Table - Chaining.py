#hashtable implemention - Chaining

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.list = []

    def __repr__(self):
        temp = self.head
        list_scheme = ''
        while True: 
            if temp.get_next() == None:
                list_scheme += str(temp)
                break
            else:
                list_scheme += str(temp)+str(" --> ")
            temp = temp.get_next()
        return list_scheme
    
    def add(self, data):
        self.list.append(Node(data))
        if len(self.list) > 1:
            self.list[-2].set_next(self.list[-1])
        else:
            self.head = self.list[0]
    
    def insert(self, data, index):
        if len(self.list) == 0:
            self.head = Node(data)
            self.list.append(self.head)
        else:
            self.list.insert(index, Node(data))
        try:
            self.list[index-1].set_next(self.list[index])
            self.list[index].set_next(self.list[index+1])
        except IndexError:
            if len(self.list) > 1:
                self.list[-2].set_next(self.list[-1])
            
    def pop(self):
        if len(self.list):
            self.list[-2].set_next(self.list[-1].get_next())
        self.list.pop()
        
    def remove(self, index):
        try:
            if len(self.list) > 1:
                self.list[index-1].set_next(self.list[index+1])
                self.list.pop(index)
            else:
                self.list.pop(index)
                self.head = None
        except IndexError:
            self.pop()
    def size(self):
        return len(self.list)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def __repr__(self):
        max_len = 8
        hash_table_scheme = ''
        i = 0
        for ll in self.table:
            hash_table_scheme += '|'+str(i).rjust(4) + '|'.center(8)
            if ll != None:
                temp = ll.list[0]
                list_scheme = ''
                while True: 
                    if temp.get_next() == None:
                        list_scheme += str(temp)
                        break
                    else:
                        list_scheme += str(temp)+str(" --> ")
                    temp = temp.get_next()
                if len(list_scheme) > max_len:
                    max_len = len(list_scheme)
                hash_table_scheme += list_scheme + '\n'
            else:
                hash_table_scheme += 'None' + '\n'
            i += 1
        hash_table_scheme = '|'+'Index'.rjust(6)+ '|'.center(4) +'Item'.rjust(6)+'\n'+'|'+'-'*7+'|'+'-'*(max_len+4)+'\n' + hash_table_scheme
        return hash_table_scheme

    def hash_(self, item):
        return sum([ord(char) for char in str(item)])%self.size
    
    def insert(self, item):
        index = self.hash_(item)
        if self.table[index] == None:
            temp = LinkedList()
            head = Node(item)
            temp.add(head)
            self.table.pop(index)
            self.table.insert(index, temp)
        else:
            self.table[index].add(Node(item))

    def search(self, item):
        index = self.hash_(item)
        message = False
        for i in self.table[index].list:
            if str(i.data) == item:
                message = True
                break
            else:
                message = False
        return message
        
    def delete(self, item):
        index = self.hash_(item)
        I = 0
        for i in self.table[index].list:
            if str(i.data) == item:
                self.table[index].remove(I)
                break
            else:
                pass
            I += 1
            
ht = HashTable(8)
ht.insert('marco')
ht.insert('newgate')
ht.insert('beckmann')
ht.insert('doflamingo')
ht.insert('shanks')
ht.insert('jack')
ht.insert('smoker')
ht.insert('sabo')
ht.insert('linlin')
ht.insert('kaido')

print(ht)

