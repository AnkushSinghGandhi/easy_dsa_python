class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.head.next = self.head

    def insert_at_head(self, data):
        "Method to insert new node at beginning of the linked list"
        new_node = Node(data)
        new_node.next = self.head
        current = self.head
        while(current):
            if current.next == self.head:
                break
        current.next = new_node
        self.head = new_node

    def insert_at_index(self, data, index):
        "Method to insert data at a specific index"
        current_index = 0
        current = self.head
        while(current):
            if current_index == index:
                break
            current_index += 1
            current = current.next
        if isinstance(data, list):
            temp = current.next
            for i in data:
                current.next = Node(i)
                current = current.next
            current.next = temp
        else:
            temp = current.next
            current.next = Node(data)
            current.next.next = temp

    def insert_at_tail(self, data):
        "Method to insert new nod at the end of linked list"
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        current = self.head

        while(current.next):
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def search(self, data):
        "Method to find a index of a given node"
        index = 0
        current = self.head
        while(current):
            if current.data == data:
                return index
            current = current.next
            index += 1

    def remove(self, key):
        "Method to remove the given node from linked list"
        current = self.head
        previous = None

        # Check if the head node is the one to be removed
        if current is not None and current.data == key:
            self.head = current.next  # Change head
            current = None  # Free the old head
            return

        # Traverse the list to find the node to be removed
        while current is not None:
            if current.data == key:
                break
            previous = current
            current = current.next

        # If the key was not present in the linked list
        if current is None:
            return

        # Unlink the node from the linked list
        previous.next = current.next
        current = None

    def remove_head(self):
        "Method to remove first element of the linked list"
        current = self.head
        if current is not None:
            self.head = current.next
            current = None

    def remove_tail(self):
        "Method to remove last element of the linked list"
        current = self.head
        while(current.next):
            previous = current
            current = current.next

        previous.next = self.head
        current = None

    def reverse(self):
        "Method to reverse the linked list"
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  # Save next node
            current.next = prev  # Reverse current node's pointer
            prev = current  # Move pointers one step forward
            current = next_node
        self.head = prev  # Update head to new first element

    def is_empty(self):
        "Method to check if the linked list is empty or not"
        return self.head is None

    def get_at_index(self, index):
        "Method to get a node at a given index"
        current_index = 0
        current = self.head
        while(current):
            if current_index == index:
                return current.data
            current = current.next
            index += 1

    def get_size(self):
        "Method to get size of the linked list"
        current = self.head
        size = 0
        while current:
            current = current.next
            size += 1
        return size

    def clear(self):
        "Method to clear linked list elements"
        self.head = None

    def clone(self):
        "Method to return a deep copy of the linked list"
        if not self.head:
            return CircularLinkedList()
        
        new_list = CircularLinkedList()
        current = self.head
        new_list.head = Node(current.data)
        new_current = new_list.head

        while current.next:
            current = current.next
            new_node = Node(current.data)
            new_current.next = new_node
            new_current = new_current.next

        return new_list

    def update_at_index(self, data, index):
        "Method to update the data of a node at a given index"
        current_index = 0
        current = self.head
        while(current):
            if current_index == index:
                current.data = data
            current = current.next

    def for_each(self, func):
        "Method to apply a function to each node's data in the linked list"
        current = self.head
        while(current):
            current.data = func(current.data)
            current = current.next

    def traverse(self):
        "Method to print the linked list"
        current = self.head         # Start from the head
        while current:              # Traverse the list until the end
            print(current.data, end=" -> ") # Print the data of each node
            current = current.next     # Move to the next node
