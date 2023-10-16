# In this I am going to create a Basic LinkedList Structure
# After that I will implement operations on that list.

# Basic Structure for node of Linked List.
class Node:
    
    def __init__(self, value, next = None) -> None:
        """
        Initialize a Node with a value and an optional reference to the next node.

        :param value: The value to store in the node.
        :param next_node: A reference to the next node in the linked list.
        """
        self.value = value
        self.next  = next
    
    def __str__(self) -> str:
        """
        Return a string representation of the node's value.
        example: print(Node(4)) -> 4
        """
        return str(self.value)
    

# Structures for LinkedList
class LinkedList:
    def __init__(self, head = None) -> None:
        """
        Initialize a linked list with an optional head node.
        :param head: The head node of the linked list.
        """
        self.head = head

    def add(self, value):
        """
        Adds a new value to the end of the linked list.

        If the linked list is empty (head is None), create a new node with the given value as the head.
        If the linked list is not empty, traverse the list to find the last node and insert the new node after it.

        :param value: The value to be added to the linked list.
        """
        if self.head is None:  # Check if the list is empty
            self.head = Node(value)
            return

        # If the list is not empty, find the last element (node) to insert the new node after it
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)
    

    def length(self):
        """
        Returns the length of the linked list.

        Returns:
        int: The number of nodes in the linked list.
        """
        count = 0
        current = self.head 
        while current:
            count += 1
            current = current.next
        return count
    
    def pop(self, index = None):
        """
        Remove and return the element at the specified index.

        Args:
        - index (int, optional): The index of the element to be removed. If None, it removes the last element.

        Returns:
        - The value of the removed element.

        Raises:
        - IndexError: If the provided index is out of range.

        """
        if self.head == None: # if list is empty
            print("Nothing to pop")
            raise IndexError("pop from empty")

        if index == 0 or self.length() == 1: # if we have to pop first element
            value = self.head.value
            self.head = self.head.next
            return value
    
        # either the index is not given or index is given but it is last index
        # in both cases we have to do same operation
        current = self.head
        previous = None
        if not index or index == self.length() - 1:
            while current.next:
                previous = current
                current = current.next
            value = current.value
            previous.next = None
            return value
        
        if 0 <= index  < self.length():
            i = 0
            while i != index:
                previous = current
                current = current.next
                i += 1
            value = current.value
            previous.next = current.next
            return value
        
        else:
            print("Index out of range, length is ", self.length())
            raise IndexError("Index out of range")
    


    def insert(self, value, index):
        """
        Inserts the element at specific index
        Args:
        - index (int): The index at which element will get inserted.
        - value (Object): Value to be inserted.
        """
        # Check if index is out of range
        if index < 0 or index > self.length():
            print("Index out of range, length is ", self.length())
            raise IndexError("Index out of range")
    
        # If index is 0, insert at the beginning of the list
        if index == 0:
            self.head = Node(value, self.head)
            return
        
        # Traverse the list until the desired index is reached
        current = self.head
        previous = None

        while index > 0:
            index -= 1
            previous = current
            current = current.next

        # Insert the new node at the desired index
        previous.next = Node(value, current)

    def remove(self, value):
        """
        removes the given value from the list
        Args:
        - value: value which will be removed
        """

        current = self.head
        previous = None
        found = False
        while current:
            if current.value == value:
                found = True
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                break
            previous = current
            current = current.next
        
        if not found:
            print(f"{value} not found in the list")
            raise ValueError("Value not found")
    
    def reverse(self):
        """
        Method performs an in-place reverse of linkedlist
        """
        if not (self.head and self.head.next):
            return
        
        current = self.head
        previous = None
        next = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    
    def __str__(self) -> str:
        """
        Return a string representation of the LinkedList.
        """
        current = self.head
        list_string = ''
        while current != None:
            list_string += str(current.value) # Convert the value to a string
            if current.next: # adding a separator
                list_string += "-->"
            current = current.next
        return list_string