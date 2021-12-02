

class vertex(object):
    def __init__(self, value):
        self.value = value
        self.edges = set()
        
    def __str__(self):
        return str(self.value)
    
    def add_edge(self, vert):
        if type(vert) is not vertex:
            print(f"Error: Argument should be of type <vertex>.")
        else:
            self.edges.add(vert)

class graph(vertex):
    def __init__(self, size):
        self.size = size
        self.vertices = set()

    def add_vertex(self, vert):
        if type(vert) is not vertex:
            print(f"Error: Argument should be of type <vertex>.")
        else:
            if len(self.vertices) < self.size:
                self.vertices.add(vert)
            else:
                print("Graph full.")

a = vertex(12)
b = vertex(23)
c = vertex(8)
d = vertex(16)

a.add_edge(b)
a.add_edge(c)
a.add_edge(d)
b.add_edge(c)
c.add_edge(d)

g = graph(4)

g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)

