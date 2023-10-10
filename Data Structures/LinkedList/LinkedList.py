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

    def __str__(self) -> str:
        """
        Return a string representation of the LinkedList.
        """
        temp = self.head
        list_string = ''
        while temp:
            list_string += str(temp.value) # Convert the value to a string
            if temp.next: # adding a separator
                list_string += "-->"
            temp = temp.next
        return list_string


print(LinkedList(Node(4, Node(5, Node(6)))))