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
        pass
    def size(self):
        pass
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

