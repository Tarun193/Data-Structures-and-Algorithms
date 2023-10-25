"""
Pronlem: https://leetcode.com/problems/merge-two-sorted-lists/
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example: 
Input: list1 = [1,2], list2 = [2,3,4]
Output: [1,1,2,3,4,4]

To solve this problem, we will traverse both lists using pointers to compare the elements of the lists.

Let's suppose we have two pointers:

i for list1
j for list2

We will compare the values at the current positions of i and j. If the value in list1 is lower than the value in list2, we will add the value from list1 to the merged list and move the i pointer to the next element. However, the j pointer will remain at its current position since we haven't merged that element yet. We will continue this process until all elements from one or both lists are consumed.

There might be a situation where all elements from one list are consumed. In this case, we will check if there are elements remaining in the other list. If so, we will add them to the merged list as there are no more elements to compare.

Lets debug example:
iteration 1:
    list1.value < list2.value -> (1 < 2) true
    merged_list.next = Node(list1.value), creating a element node and adding it to next of current element in merged_list.
    list1 = list1.next , moving to next element
    merged_list = merged_list.next, as next element will be added at last element's next.
    mereged_list = [1]

    iteration 2:
    list1.value < list2.value -> (2 < 2) false
    merged_list.next = Node(list2.value), creating a element node and adding it to next of current element in merged_list.
    list2 = list2.next , moving to next element
    merged_list = merged_list.next, as next element will be added at last element's next.
    mereged_list = [1, 2]

    iteration 3:
    list1.value < list2.value -> (2 < 3) true
    merged_list.next = Node(list1.value), creating a element node and adding it to next of current element in merged_list.
    list1 = list1.next , moving to next element
    merged_list = merged_list.next, as next element will be added at last element's next.
    mereged_list = [1,2,2]

    Now the first is fully consumed and our first will loop will stop as condition is false now.
    Now we will just add 2,4 into mereged list.
    mereged_list = [1,2,2,3,4]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
        # Create an empty merged_list and a temp pointer to keep track of the head
        merged_list = ListNode()
        temp = merged_list
        while list1 and list2:
            if list1.val > list2.val:
                merged_list.next = ListNode(list2.val)
                list2 = list2.next
                merged_list = merged_list.next
            else:
                merged_list.next = ListNode(list1.val)
                list1 = list1.next
                merged_list = merged_list.next
        # If elements left in first list
        while list1:
            merged_list.next = ListNode(list1.val)
            list1 = list1.next
            merged_list = merged_list.next
            
        # If elements left in second list.
        while list2:
            merged_list.next = ListNode(list2.val)
            list2 = list2.next
            merged_list = merged_list.next
        
        return temp.next