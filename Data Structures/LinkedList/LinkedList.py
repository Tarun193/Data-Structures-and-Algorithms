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
    
    class LinkedList:
        def __init__(self):
            self.head = None

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


