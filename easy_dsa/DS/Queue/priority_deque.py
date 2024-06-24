class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
        self.prev = None

class PriorityDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        "Method to check if queue is empty"
        return self.size == 0

    def enqueue_front(self, data, priority):
        "Method to insert a node from the front"
        new_node = Node(data, priority)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            current = self.front
            while current and current.priority >= priority:
                current = current.next
            if current == self.front:  # New node has the highest priority
                new_node.next = self.front
                self.front.prev = new_node
                self.front = new_node
            elif current is None:  # New node has the lowest priority
                self.rear.next = new_node
                new_node.prev = self.rear
                self.rear = new_node
            else:  # Insert in the middle
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
        self.size += 1

    def enqueue_rear(self, data, priority):
        "Method to insert a node from the rear"
        new_node = Node(data, priority)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            current = self.rear
            while current and current.priority <= priority:
                current = current.prev
            if current == self.rear:  # New node has the lowest priority
                new_node.prev = self.rear
                self.rear.next = new_node
                self.rear = new_node
            elif current is None:  # New node has the highest priority
                self.front.prev = new_node
                new_node.next = self.front
                self.front = new_node
            else:  # Insert in the middle
                new_node.prev = current
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
        self.size += 1

    def dequeue_front(self):
        "Method to remove a node from the front"
        if self.is_empty():
            raise IndexError("Dequeue from empty deque")
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        self.size -= 1
        return dequeued_node.data

    def dequeue_rear(self):
        "Method to remove a node from the rear"
        if self.is_empty():
            raise IndexError("Dequeue from empty deque")
        dequeued_node = self.rear
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        self.size -= 1
        return dequeued_node.data

    def traverse(self):
        "Method to traverse the queue"
        current = self.front
        while current:
            print(f"({current.data}, {current.priority})", end=" -> ")
            current = current.next
        print("NULL")

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Get rear from empty deque")
        return self.rear.data

    def get_size(self):
        "Method to check size of the queue"
        return self.size

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

    def contains(self, data):
        "Method to check if the queue contains the value"
        current = self.front
        while(current):
            if current.data == data:
                return True
            current = current.next
        return False

    def clear(self):
        "Method to clear entire Queue"
        self.front = self.rear = None
        self.count = 0
