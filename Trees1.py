"""
struct BST {
    BST* left
    BST* right
}
"""


class BST(object):
    """
    void Insert (int key, int value)
    (int value) Find (int key)
    bool Delete (int key)
    void printTree
    """

    
    def __init__(self):
        self.key = None
        self.value = None
        self.left = None
        self.right = None


    def insert(self, key, value):
        if self.key is None:
            self.key = key
            self.value = value
        else:
            if e < self.key:
                if self.left is None:
                    self.left = BST(e)
                else:
                    self.left.insert(e)
        
            elif e > self.key:
                if self.right is None:
                    self.right = BST(e)
                else:
                    self.right.insert(e)
            # Note that nothing happens if e is equal to node key.

    def printKeys(self):
        if self.key is None:
            print("tree is empty")
        else:
            if self.left is not None: self.left.printTree()
            print(self.key)
            if self.right is not None: self.right.printTree()




class Person(object):

    def __init__(self, name):
        self.name = name
        self.address = 'sljkdflfjslkdfjfd'





class PersonIndex(object):



    def __init__(self, yo):
        self.byname = BST()
        self.byaddress = BST()

        
    def insert(self, p):
        self.byname.insert(p.name, p)
        self.byaddress.insert(p.address, p)



"""
obj = PersonIndex()
obj.byname
"""

        

if __name__ == "__main__":
    people = [Person('kanu'), Person('sonu')]

    index = PersonIndex()
    
    for p in people:
        index.insert(p)

    index.findByAddress(...)

    obj.find('kanu')
    
     
