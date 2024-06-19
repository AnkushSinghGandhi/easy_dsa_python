from queue import Queue

class PopEfficientStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def is_empty(self):
        "Method to check if stack is empty or not"
        return self.queue1.empty() and self.queue2.empty()

    def push(self, data):
        "Method to push new node in the stack"
        self.queue2.put(data)
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
        self.queue1, self.queue2 = self.queue2, self.queue1  # Always keep queue1 as the main queue

    def pop(self):
        "Method to pop the top node in the stack"
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.queue1.get()

    def peek(self):
        "Method to check top node"
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.queue1.queue[0]

    def get_size(self):
        "Method to get size of the stack"
        return self.queue1.qsize()

    def traverse(self):
        "Method to traverse the stack"
        temp_queue = Queue()
        while not self.queue1.empty():
            item = self.queue1.get()
            print(item, end=" ")
            temp_queue.put(item)
        print()
        self.queue1, temp_queue = temp_queue, self.queue1
