#Graph implemention - Adjacency List 

class Node:

    def __init__(self, data):
        self.data = data
        self.edge = []
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

     
class Graph(Node, LinkedList):

    def __init__(self, size):
        self.size = size
        self.vertices = []
        self.list = [LinkedList() for _ in range(size)]
        
    def __repr__(self):
        graph_scheme = ''
        i = 0
        for vertex in self.vertices:
            graph_scheme += str(i)+"|  "
            graph_scheme += str(self.list[i])
            graph_scheme += '\n'
            i += 1
        return graph_scheme
    
    def add_vertex(self, node):
        if len(self.vertices) < self.size:
            self.vertices.append(node)
        else:
            print('Graph full!')

    def add_edge(self,node,destination):
        self.vertices[node].edge.append(self.vertices[destination])
        self.list[node].add(destination)
        
    def display_vertex(self,index):
        node = self.vertices[index]
        return "node("+str(type(node.data))[8:-2]+"("+str(node.data)+")"+")"

g = Graph(4)
g.add_vertex(Node("213"))
g.add_vertex(Node(True))
g.add_vertex(Node(21))
g.add_vertex(Node(None))
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,0)
print(g.display_vertex(0))
print(g)
