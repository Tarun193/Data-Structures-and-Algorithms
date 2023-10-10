# In this I am going to create a Basic LinkedList Structure
# After that I will implement operations on that list.

# Basic Structure for node of Linked List.
class Node:
    # Constructor for Node
    # While creating node, the next of node can be null.
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next  = next
    
    # This methods gives the String repersentation of the object
    # So when even some will call print method on the Node object,
    # It will print node's value
    # For example print(Node(4)) -> 4
    def __str__(self) -> str:
        return str(self.value)