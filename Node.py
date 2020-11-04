class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,new_data):
        self.data = new_data

    def set_next(self,new_next):
        self.next = new_next


class LinkedList(Node):
    def __init__(self):
        self.head = Node()
        self.items = []
        
    def __repr__(self):
        return ' --> '.join([item.data for item in self.items])

    def add(self,item):
        if self.head.data == None:
            self.head.set_data(item)
            self.head.set_next(None)
            self.items.append(self.head)
            
        else:
            temp = Node()
            temp.set_data(item)
            self.items.append(temp)
            self.items[-2].set_next(temp)
    def pop(self):
        self.items[-2].set_next(None)
        self.items.pop()

    def size(self):
        return len(self.items)

    def insert(self,index,item):
        temp = Node()
        temp.set_data(item)
        assert type(index) == int , 'Must be integer'
        self.items.insert(index,temp)
        if self.items[0] == temp:
            temp.set_next(self.items[1])
        elif self.items[-1] == temp:
            self.items[index - 1].set_next(temp)
        else:
            temp.set_next(self.items[index + 1])
            self.items[index - 1].set_next(temp)
        
        
l1 = LinkedList()
l1.add("1")
l1.add("2")
l1.add("3")
l1.pop()
l1.insert(1, "5")

print(l1)


        
