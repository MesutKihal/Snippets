class Stack:
    def __init__(self):
        self.items = []
        
    def __repr__(self):
        return ' '.join(self.items)
    
    def is_empty(self):
        self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



s1 = Stack()

s1.push("1")
s1.push("8")
s1.push("13")

print(s1)



        
