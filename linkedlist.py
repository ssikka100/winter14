class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    """If list is empty, then start will be None.
    If start is not None, then end will not be None."""
    def __init__(self, first_node, last_node):
        self.start = first_node
        self.end = last_node

    def clone(self):
        if self.start is None:
            return LinkedList (None, None)
        currNode = self.start
        cloneStart = None
        cloneEnd = None
        
        while currNode is not None:
            NewCloneNode = Node(currNode.value)
            
            if cloneEnd is not None:
                cloneEnd.next = NewCloneNode
                cloneEnd = NewCloneNode

            if cloneStart is None:
                cloneStart = NewCloneNode
                cloneEnd = NewCloneNode          

            currNode = currNode.next
            
        return LinkedList(cloneStart,cloneEnd)
            
        
    def size(self):
        currNode = self.start
        count =0
        while currNode is not None:
            count += 1
            currNode=currNode.next
            
        return count
 
    def reverse(self):
        pass


    ## only for testing purposes
    @staticmethod
    def from_list(l):
        """Turns a python list to our linkedlist"""
        first_node = None
        last_node = None

        for value in l:
            new_node = Node(value)
            if last_node is not None:
                last_node.next = new_node

            if first_node is None:
                first_node = new_node

            last_node = new_node

        return LinkedList(first_node, last_node)

    def to_list(self):
        values = []
        cur_node = self.start
        while cur_node is not None:
            values.append(cur_node.value)
            if cur_node is self.end:
                break
            cur_node = cur_node.next
        return values


import unittest

class FromListTest(unittest.TestCase):
    def test_from_list(self):
        l = [1,2,3]
        ll = LinkedList.from_list(l)
        self.assertEqual(ll.start.value, 1)
        self.assertEqual(ll.start.next.value, 2)
        self.assertEqual(ll.start.next.next.value, 3)
        self.assertEqual(ll.start.next.next, ll.end)

        self.assertListEqual(ll.to_list(), l)

    def test_from_empty_list(self):
        ll = LinkedList.from_list([])
        self.assertIsNone(ll.start)
        self.assertIsNone(ll.end)

    def test_from_singleton_list(self):
        ll = LinkedList.from_list([989])
        self.assertIsNotNone(ll.start)
        self.assertEqual(ll.start, ll.end)

class SizeTest(unittest.TestCase):
    def test_size_of_empty(self):
        ll = LinkedList.from_list([])
        self.assertEqual(ll.size(), 0)

    def test_size_of_singleton(self):
        ll = LinkedList.from_list([989])
        self.assertEqual(ll.size(), 1)

    def test_size_of_big(self):
        ll = LinkedList.from_list([989,3,4,5,5,5])
        self.assertEqual(ll.size(), 6)

class CloneTest(unittest.TestCase):
    def test_clone_empty(self):
        ll1 = LinkedList.from_list([])
        ll2 = ll1.clone()
        self.assertNotEqual(ll1,ll2)

    def test_clone_singleton(self):
        ll1 = LinkedList.from_list([])
        ll2 = ll1.clone()
        self.assertNotEqual(ll1,ll2)
        self.assertNotEqual(ll1.start,ll2.start)
        self.assertListEqual(ll1.to_list(), ll2.to_list())

if __name__ == "__main__":
    unittest.main()

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    """If list is empty, then start will be None.
    If start is not None, then end will not be None."""
    def __init__(self, first_node, last_node):
        self.start = first_node
        self.end = last_node

    @staticmethod
    def from_list(l):
        """Turns a python list to our linkedlist"""
        first_node = None
        last_node = None

        for value in l:
            new_node = Node(value)
            if last_node is not None:
                last_node.next = new_node

            if first_node is None:
                first_node = new_node

            last_node = new_node

        return LinkedList(first_node, last_node)

    def to_list(self):
        values = []
        cur_node = self.start
        while cur_node is not None:
            values.append(cur_node.value)
            if cur_node is self.end:
                break
            cur_node = cur_node.next
        return values

import unittest

class LinkedListTest(unittest.TestCase):
    def test_from_list(self):
        l = [1,2,3]
        ll = LinkedList.from_list(l)
        self.assertEqual(ll.start.value, 1)
        self.assertEqual(ll.start.next.value, 2)
        self.assertEqual(ll.start.next.next.value, 3)
        self.assertEqual(ll.start.next.next, ll.end)
        self.assertListEqual(ll.to_list(), l)

if __name__ == "__main__":
    unittest.main()

