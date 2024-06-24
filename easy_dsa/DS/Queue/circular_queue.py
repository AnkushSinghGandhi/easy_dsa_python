class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        "Method to check if queue is empty"
        return self.size == 0

    def enqueue(self, data):
        "Method to add a new node"
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
        self.size += 1

    def dequeue(self):
        "Method to remove the first node"
        if self.is_empty():
            raise IndexError("Circular Queue is empty")
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.size -= 1
        return data

    def peek_front(self):
        "Method to get first node of the queue"
        if self.is_empty():
            raise IndexError("Circular Queue is empty")
        return self.front.data

    def peek_rear(self):
        "Method to get last node of the queue"
        if self.is_empty():
            raise IndexError("Circular Queue is empty")
        return self.rear.data

    def traverse(self):
        "Method to traverse the queue"
        if self.is_empty():
            print("Circular Queue is empty")
            return
        current = self.front
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.front:
                break
        print("NULL")

    def get_size(self):
        "Method to check size of the queue"
        return self.size

    def clear(self):
        "Method to clear entire Queue"
        self.front = self.rear = None
        self.size = 0

    def contains(self, data):
        "Method to check if the queue contains the value"
        if self.is_empty():
            return False
        current = self.front
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.front:
                break
        return False