class queuelist:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) 
        else:
            raise IndexError("dequeue from an empty queue")
    def peek(self):
        if not self.is_empty():
            return self.items[0] 
        else:
            raise IndexError("peek forms an empty stack")
    def size(self):
        return len(self.items)
queue=queuelist()
queue.enqueue(1) 
queue.enqueue(2)
queue.enqueue(3)
print("front of the queue",queue.peek())
print("dequeue",queue.dequeue())
print("size of the queue",queue.size())