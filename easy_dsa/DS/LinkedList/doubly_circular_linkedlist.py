class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def insert_at_head(self, data):
        "Method to insert a new node at the beginning of the linked list"
        new_node = Node(data)
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, data, index):
        "Method to insert data at a specific index"
        current_index = 0
        current = self.head
        while current:
            if current_index == index:
                break
            current_index += 1
            current = current.next

        if isinstance(data, list):
            temp = current.next
            for i in data:
                current.next = Node(i)
                current.next.previous = current
                current = current.next
            current.next = temp
            if temp:
                temp.previous = current
        else:
            temp = current.next
            current.next = Node(data)
            current.next.previous = current
            current.next.next = temp
            if temp:
                temp.previous = current.next

    def insert_at_tail(self, data):
        "Method to insert a new node at the end of the linked list"
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.previous = current

    def search(self, data):
        "Method to find the index of a given node"
        index = 0
        current = self.head
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1  # Return -1 if data is not found

    def remove(self, key):
        "Method to remove the given node from the linked list"
        current = self.head

        # Check if the head node is the one to be removed
        if current is not None and current.data == key:
            self.head = current.next  # Change head
            if self.head is not None:
                self.head.previous = None
            current = None  # Free the old head
            return

        # Traverse the list to find the node to be removed
        while current is not None:
            if current.data == key:
                break
            current = current.next

        # If the key was not present in the linked list
        if current is None:
            return

        # Unlink the node from the linked list
        if current.previous is not None:
            current.previous.next = current.next
        if current.next is not None:
            current.next.previous = current.previous
        current = None

    def remove_head(self):
        "Method to remove the first element of the linked list"
        current = self.head
        if current is not None:
            self.head = current.next
            if self.head is not None:
                self.head.previous = None
            current = None

    def remove_tail(self):
        "Method to remove the last element of the linked list"
        current = self.head
        if current is None:
            return  # List is empty
        if current.next is None:
            self.head = None  # List has only one node
            return
        while current.next:
            previous = current
            current = current.next
        previous.next = None
        current = None

    def reverse(self):
        "Method to reverse the linked list"
        previous_node = None
        current = self.head
        while current is not None:
            next_node = current.next  # Save next node
            current.next = previous_node  # Reverse current node's pointer
            current.previous = next_node  # Correctly set the previous pointer
            previous_node = current  # Move pointers one step forward
            current = next_node
        self.head = previous_node  # Update head to the new first element

    def is_empty(self):
        "Method to check if the linked list is empty or not"
        return self.head is None

    def get_at_index(self, index):
        "Method to get a node's data at a given index"
        current_index = 0
        current = self.head
        while current:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1
        return None  # Handle the case when index is out of bounds

    def get_size(self):
        "Method to get the size of the linked list"
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
            return DoublyLinkedList()

        new_list = DoublyLinkedList()
        current = self.head
        new_list.head = Node(current.data)
        new_current = new_list.head

        while current.next:
            current = current.next
            new_node = Node(current.data)
            new_current.next = new_node
            new_node.previous = new_current
            new_current = new_current.next

        return new_list

    def update_at_index(self, data, index):
        "Method to update the data of a node at a given index"
        current_index = 0
        current = self.head
        while current:
            if current_index == index:
                current.data = data
                return  # Stop the loop once the data is updated
            current = current.next
            current_index += 1

    def for_each(self, func):
        "Method to apply a function to each node's data in the linked list"
        current = self.head
        while current:
            current.data = func(current.data)
            current = current.next

    def traverse(self):
        "Method to print the linked list"
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("NULL")