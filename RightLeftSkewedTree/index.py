class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
    
class BinarTree:

    def __init__(self):
        self.root = None
    
    def addLeftSkewed(self , data):
        newNode = Node(data)
        if(self.root is None):
            self.root = newNode
            return
        temp = self.root
        while(temp.left is not None):
            temp = temp.left
        temp.left = newNode
        newNode.left = None

    def addRightSkewed(self , data):
        newNode = Node(data)
        if(self.root is None):
            self.root = newNode
            return
        temp = self.root
        while(temp.right is not None):
            temp = temp.right
        temp.right = newNode
        newNode.right = None