
class Queue:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return "Queue: ["+', '.join([str(i) for i in self.items])+"]"

    def isfull(self):
        if len(self.items) >=1 :
            return True
        else:
            return False
        
    def isempty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if len(self.items) >= 1:
            self.items.pop(0)

    def peek(self):
        if len(self.items) >= 1:
            return self.items[0]
        else:
            return None

queue = Queue()
queue.enqueue(8)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(7)
queue.dequeue()
print(queue.peek())
print(queue)

