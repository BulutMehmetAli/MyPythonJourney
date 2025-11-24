from collections import deque

class Node:
    def __init__(self , data):
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
        myQueue = deque()
        myQueue.append(self.root)
        while myQueue:
            temp = myQueue.popleft()
            if temp.left is None:
                temp.left = newNode
                return
            else:
                myQueue.append(temp.left)
            if temp.right is None:
                temp.right = newNode
                return
            else:
                myQueue.append(temp.right)
    
    def showTrees(self):
        if self.root is None:
            return
        myQueue = deque()
        myQueue.append(self.root)
        while myQueue:
            temp = myQueue.popleft()
            print(temp.data , end=" -> ")
            if temp.left:
                myQueue.append(temp.left)
                
            if temp.right:
                myQueue.append(temp.right)
                
   
    def binarySearchAddNode(self , value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return
        
        temp = self.root
        boolValue = True
        while True:
            if value > temp.data:
                if temp.right is None:
                    temp.right = newNode
                    return
                temp = temp.right
                    
            else:
                if temp.left is None:
                    temp.left = newNode
                    return
                temp = temp.left
            
    def inOrder(self , node):
        if self.root is None:
            return
        temp = node
        
        if temp.left:
            self.inOrder(temp.left)
        print(temp.data , end= " -> ")
        if temp.right:
            self.inOrder(temp.right)
       
    def inOrders(self , node):
        if node is None:
            return
       
        self.inOrders(node.left)
        print(node.data , end= " -> ")
        self.inOrders(node.right)
        

    def preOrder(self , node):
        if node is None:
            return
        print(node.data , end= " -> ")
        self.preOrder(node.left)
        self.preOrder(node.right)
    
    def postOrder(self , node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data , end= " -> ")

    def levelOrderRec(self , root , level , res):
        if root is None:
            return
        # Add a new level to the result if needed
        if len(res) <= level:
            res.append([])
        
        # Add current node's data to its coreesponding level
        res[level].append(root.data)

        # Recur for left and right children 
        self.levelOrderRec(root.left , level+1 , res)
        self.levelOrderRec(root.right , level+1 , res)


    def levelOrder(self , root):
        # Stores the result level by level
        res = []
        self.tryOne(root , 0 , res)
        return res

    def tryOne(self , root , level , res):
        if root is None:
            return
        if len(res) <= level:
            res.append([])
        
        res[level].append(root.data)

        self.tryOne(root.left , level+1 , res)
        self.tryOne(root.right , level+1 , res)
    
    def rec(self , root):
        if root is None:
            return None
        res = []
        self.tryOne(root , 0 , res)
        return res
myTree = Tree()

myTree.binarySearchAddNode(10)
myTree.binarySearchAddNode(5)
myTree.binarySearchAddNode(20)
myTree.binarySearchAddNode(15)
myTree.binarySearchAddNode(8)
myTree.binarySearchAddNode(7)
myTree.binarySearchAddNode(9)
myTree.binarySearchAddNode(3)
myTree.binarySearchAddNode(1)
myTree.binarySearchAddNode(2)

print(myTree.rec(myTree.root))         
