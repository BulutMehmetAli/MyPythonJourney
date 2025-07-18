from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    
    def addNode(self , data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        temp = self.root
        while(True):
            if(data < temp.data):
                if temp.left is None:
                    temp.left = newNode
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    return
                temp = temp.right 
    def inOrder(self, head):
        if head is None:
            return
        self.inOrder(head.left)
        print(head.data, end=' ')  
        self.inOrder(head.right)    
    
    def preOrder(self, head):
        if head is None:
            return
        print(head.data, end=' ') 
        self.preOrder(head.left)
        self.preOrder(head.right)    
    
    def postOrder(self, head):
        if head is None:
            return
        self.postOrder(head.left)
        self.postOrder(head.right) 
        print(head.data, end=' ') 

    def levelOrderTraverse(self , head):
        if self.root is None:
            return
        q = deque()
        q.append(head)
        
        while len(q) > 0:
            temp = q.popleft()
            print(temp.data  , end= " ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

    def deepthTree(self , head):
        if head is None:
            return 0
        left = self.deepthTree(head.left)
        right = self.deepthTree(head.right)

        return 1 + max(left , right)
    
    def printGivenLevel(self , head , level):
        if head is None:
            return
        if level == 1:
            print(head.data)
        elif level > 1:
            self.printGivenLevel(head.left , level - 1)
            self.printGivenLevel(head.right , level - 1)
    def printLevelByLevel(self , head):
        height = self.deepthTree(head)
        for i in range(1 , height + 1):
            self.printGivenLevel(head , i)
            print()
    """def queueWithDelimiter(self , head , level):
        if self.root is None:
            return
        q = deque()
        q.append(head)
        
        if(level == 1 ):
            print(he)


        while q.
            temp = q.popleft()
            print(temp.data  , end= " ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)"""
        
myTree = Tree()
myTree.addNode(10)
myTree.addNode(7)
myTree.addNode(14)
myTree.addNode(6)
myTree.addNode(8)
myTree.addNode(5)
myTree.addNode(9)
myTree.addNode(13)
myTree.addNode(16)
myTree.addNode(28)

deepth = myTree.deepthTree(myTree.root)
myTree.printLevelByLevel(myTree.root , deepth)
