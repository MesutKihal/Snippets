#Linked List implemention

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

l = LinkedList()
l.insert(Node(0), 0)
l.insert(Node(True), 2)
l.insert(Node("1"), 1)
l.insert(Node(2.16), 3)
print(l)
