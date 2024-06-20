class Node:
    def __init__(self, data, priority):
        self.data = data
        self.next = None
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

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

    def reverse(self):
        "Method to reverse the queue"
        prev = None
        current = self.front
        self.rear = self.front
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.front = prev

    def traverse(self):
        "Method to traverse the queue"
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next

    def enqueue(self, data, priority):
        "Method to add a new node"
        new_node = Node(data, priority)

        if self.is_empty() or self.front.priority < priority:
            new_node.next = self.front
            self.front = new_node
        else:
            current = self.front
            while current.next and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.count += 1

    def dequeue(self):
        "Method to remove the first node"
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        return dequeued_node.data

    def is_empty(self):
        "Method to check if queue is empty"
        return self.front is None

    def get_size(self):
        "Method to check size of the queue"
        return self.count

    def get_front(self):
        "Method to get first node of the queue"
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.front.data