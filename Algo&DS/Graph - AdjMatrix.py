#Graph implemention - Adjacency Matrix

class Node:

    def __init__(self, data):
        self.data = data
        self.edge = []
        
    def __repr__(self):
        return str(self.data)
        
class Graph(Node):

    def __init__(self, size):
        self.size = size
        self.vertices = []
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]
        
    def __repr__(self):
        graph_scheme = ' '*4+'  '.join([str(i) for i in range(len(self.vertices))])+'\n'
        i = 0
        for vertex in self.vertices:
            graph_scheme += str(i)+"  "
            graph_scheme += str(self.matrix[i])
            graph_scheme += '\n'
            i += 1
        return graph_scheme
    
    def add_vertex(self, node):
        if len(self.vertices) < self.size:
            self.vertices.append(node)
        else:
            print('Graph full!')

    def add_edge(self,node,destination):
        self.matrix[node][destination] += 1
        self.vertices[node].edge.append(self.vertices[destination])
        
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
