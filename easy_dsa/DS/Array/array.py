class Array:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = []
        else:
            self.elements = list(elements)

    def __str__(self):
        return str(self.elements)

    def is_empty(self):
        "Method to check if array is empty or not"
        return len(self.elements) == 0

    def get_size(self):
        "Method to get size of the array"
        return len(self.elements)

    def get_element(self, index):
        "Method to get an element at an index"
        if index < 0 or index >= len(self.elements):
            raise IndexError("Index out of range")
        return self.elements[index]

    def set_element(self, index, value):
        "Method to set an element at an index"
        if index < 0 or index >= len(self.elements):
            raise IndexError("Index out of range")
        self.elements[index] = value

    def append(self, value):
        "Method to apend an element"
        self.elements.append(value)

    def insert(self, index, value):
        "Method to insert an element at particular index"
        if index < 0 or index > len(self.elements):
            raise IndexError("Index out of range")
        self.elements.insert(index, value)

    def delete(self, index):
        "Method to delete an element at particular index"
        if index < 0 or index >= len(self.elements):
            raise IndexError("Index out of range")
        del self.elements[index]

    def traverse(self):
        "Method to traverse the array"
        for element in self.elements:
            print(element, end=" ")
        print()

    def linear_search(self, value):
        "Method to find an element using linear search"
        for i, element in enumerate(self.elements):
            if element == value:
                return i
        return -1

    def binary_search(self, value):
        "Method to find an element using binary search"
        left, right = 0, len(self.elements) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.elements[mid] == value:
                return mid
            elif self.elements[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    