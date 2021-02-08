

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        if self.right and self.left:
            return str(self.value) +' '+ str(self.left.value) +' '+ str(self.right.value)
        elif self.right and not self.left:
            return str(self.value) +' '+ '*' +' '+ str(self.right.value)
        elif not self.right and self.left:
            return str(self.value) +' '+ str(self.left.value) +' '+ '*'
        else:
            return str(self.value) +' '+ '*' +' '+ '*'
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
                
    def search(self, value):
        if value < self.value:
            if self.left is None:
                print(f"Value {value} not found.")
            else:
                self.left.search(value)
        elif value > self.value:
            if self.right is None:
                print(f"Value {value} not found.")
            else:
                self.right.search(value)
        else:
            print(f"Value {value} found.")

                
root = Node(12)
root.insert(8)
root.insert(16)
root.insert(32)
root.insert(14)
root.insert(4)
root.insert(2)
root.search(2)
root.PrintTree()
print(root)
