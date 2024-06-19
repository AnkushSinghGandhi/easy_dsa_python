from queue import Queue

class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def is_empty(self):
        "Method to check if stack is empty or not"
        return self.queue1.empty()

    def push(self, data):
        "Method to push new node in the stack"
        self.queue1.put(data)

    def pop(self):
        "Method to pop the top node in the stack"
        if self.is_empty():
            raise IndexError("pop from empty stack")
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        popped_item = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_item

    def peek(self):
        "Method to check top node"
        if self.is_empty():
            raise IndexError("peek from empty stack")
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        top_item = self.queue1.get()
        self.queue2.put(top_item)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_item

    def get_size(self):
        "Method to get size of the stack"
        return self.queue1.qsize()

    def traverse(self):
        "Method to traverse the stack"
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Stack elements:", end=" ")
        
        while not self.queue1.empty():
            item = self.queue1.get()
            print(item, end=" -> ")
            self.queue2.put(item)
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        print()
