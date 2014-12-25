"""
struct BST {
    BST* left
    BST* right
}
"""


class BST(object):
    """
    void Insert int
    bool Find int
    bool Delete int
    void printTree
    """

    
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


    def depth(self):
        if self.value is None:
            return 0
        else:
            if self.left is not None:
                leftDepth = self.left.depth()
            else: leftDepth = 0
            
            if self.right is not None:
                rightDepth = self.right.depth()
            else: rightDepth = 0

            return max(leftDepth,rightDepth) + 1
        
##            
##
##    def size(self):
##        if self.value is None:
##            return 0
##        elif self.left is not None or self.right is not None:
##            return self.right.size() + self.left.size() + 1
##        else: return 0
 

    def deleteNode(self, e):
        if self.value is None:
            return None

        else:
            if e < self.value:
                self.left = self.left.deleteNode(e)


    def InorderSucc(self, search):
        if search.right is not None:
            return search.value

        while(self.value is not None):
            if self.value > seach.value:
                succ = self
                self = self.left
            if self.value < search.value:
                self = self.right
            if self.value == search.value:
                break
        return succ
            
        

    def insert(self, e):
        if self.value is None:
            self.value = e   
        else:
            if e < self.value:
                if self.left is None:
                    self.left = BST(e)
                else:
                    self.left.insert(e)
        
            elif e > self.value:
                if self.right is None:
                    self.right = BST(e)
                else:
                    self.right.insert(e)
            # Note that nothing happens if e is equal to node value.

    def printTree(self):
        if self.value is None:
            print("tree is empty")
        else:
            if self.left is not None: self.left.printTree()
            print(self.value)
            if self.right is not None: self.right.printTree()

if __name__ == "__main__":
    obj = BST()
    obj.insert(3)
    obj.insert(1)
    obj.insert(50)
    obj.insert(60)
    obj.insert(70)
    obj.printTree()
    d = obj.depth()
    print(d)
    

  
            
        
