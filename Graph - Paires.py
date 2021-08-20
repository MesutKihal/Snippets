#Graph implemention - Paires

class Node:

    def __init__(self, data):
        self.data = data
        self.edge = []
        
    def __repr__(self):
        return str(self.data)
        
class Graph(Node):

    def __init__(self):
        self.pairs = dict()
        self.vertices = []
        
    def __repr__(self):
        graph_scheme = ''
        i = 0
        for vertex in self.vertices:
            graph_scheme += str(i)+" |  "
            graph_scheme += str(self.pairs[i])
            graph_scheme += '\n'
            i += 1
        return graph_scheme
    
    def add_vertex(self, node):
        self.vertices.append(node)

    def add_edge(self,node,destination):
        try:
            self.pairs[node].add((node, destination))
        except KeyError:
            self.pairs[node] = set()
            self.pairs[node].add((node, destination))
        self.vertices[node].edge.append(self.vertices[destination])
        
    def display_vertex(self,index):
        node = self.vertices[index]
        return "node("+str(type(node.data))[8:-2]+"("+str(node.data)+")"+")"

g = Graph()
g.add_vertex(Node("213"))
g.add_vertex(Node(True))
g.add_vertex(Node(21))
g.add_vertex(Node(None))
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,0)
print(g.vertices[0])
print(g.display_vertex(0))
print(g)
