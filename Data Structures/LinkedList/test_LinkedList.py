import unittest
from LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_add(self):
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)
        self.assertEqual(str(linked_list), "1-->2-->3")
    
    def test_length(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.length(), 0)
        linked_list.add(1)
        self.assertEqual(linked_list.length(), 1)
        linked_list.add(2)
        self.assertEqual(linked_list.length(), 2)
        linked_list.add(3)
        self.assertEqual(linked_list.length(), 3)
    
    def test_pop(self):
        # Test removing the last element
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)
        linked_list.pop()
        self.assertEqual(str(linked_list), "1-->2")
        
        # Test removing the first element
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)
        linked_list.pop(0)
        self.assertEqual(str(linked_list), "2-->3")
        
        # Test removing an element at a specific index
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)
        linked_list.pop(1)
        self.assertEqual(str(linked_list), "1-->3")
        
        # Test removing the only element in the list
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.pop()
        self.assertEqual(str(linked_list), "")
        
        # Test removing from an empty list
        linked_list = LinkedList()
        with self.assertRaises(IndexError):
            linked_list.pop()
        
        # Test removing from an index that is out of range
        linked_list = LinkedList()
        linked_list.add(1)
        with self.assertRaises(IndexError):
            linked_list.pop(1)