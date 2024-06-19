class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class PushEfficientStack:
    def __init__(self, data):
        self.top = Node(data)
        self.size = 0

    def push(self, data):
        "Method to push new node in the stack"
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        "Method to get and remove the top node in the stack"
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop item.")
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item

    def is_empty(self):
        "Method to check if stack is empty or not"
        return self.size == 0
    
    def get_size(self):
        "Method to get size of the stack"
        return self.size

    def peek(self):
        "Method to check top node"
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot peek item.")
        return self.top.data

    def traverse(self):
        "Method to traverse the stack"
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")