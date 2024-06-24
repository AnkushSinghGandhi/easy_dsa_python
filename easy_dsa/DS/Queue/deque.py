class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Deque:
    def __init__(self, data):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue_front(self, data):
        "Method to insert a node from the front"
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node

        else:
            new_node.next = self.front
            self.front = new_node

        self.count += 1

    def enqueue_rear(self, data):
        "Method to insert a node from the rear"
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1

    def dequeue_front(self):
        "Method to remove a node from the front"
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        return dequeued_node.data

    def dequeue_rear(self):
        "Method to remove a node from the rear"
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        dequeued_node = self.rear
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            current = self.front
            while current.next != self.rear:
                current = current.next
            current.next = None
            self.rear = current
        
        self.count -= 1
        return dequeued_node.data

    def traverse(self):
        "Method to traverse the queue"
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next

    def is_empty(self):
        "Method to check if queue is empty"
        return self.front is None

    def get_size(self):
        "Method to check size of the queue"
        return self.count

    def peek_front(self):
        "Method to get first node of the queue"
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def peek_rear(self):
        "Method to get last node of the queue"
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.rear.data

    def clear(self):
        "Method to clear entire Queue"
        self.front = self.rear = None
        self.count = 0

    def contains(self, data):
        "Method to check if the queue contains the value"
        current = self.front
        while(current):
            if current.data == data:
                return True
            current = current.next
        return False