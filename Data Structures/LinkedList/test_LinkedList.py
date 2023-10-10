import unittest
from LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_add(self):
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)
        self.assertEqual(str(linked_list), "1-->2-->3")