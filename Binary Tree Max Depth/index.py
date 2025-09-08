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
        if self.root == None:
            self.root = newNode
            return
        q = deque([self.root])

        while q:
            temp = q.popleft()

            if temp.left is None:
                temp.left = newNode
                return
            else:
                q.append(temp.left)
            
            if temp.right is None:
                temp.right = newNode
                return
            else:
                q.append(temp.right)

    def displayLevelOrder(self):
        if self.root is None:
            return
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.data, end=" -> ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    # Preorder Traversal (NLR)
    def preOrder(self , node):
        if node is None:   # ✅ base case
            return
        print(node.data , end=" -> ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    # Inorder Traversal (LNR)
    def inOrder(self , node):
        if node is None:   # ✅ base case
            return
        self.inOrder(node.left)
        print(node.data , end=" -> ")
        self.inOrder(node.right)

    # Postorder Traversal (LRN)
    def postOrder(self , node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data , end=" -> ")
    
    def maxDepth(self , node):
        if node is None:
            return 0
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        return max( left , right) + 1




myTree = Tree() 
myTree.addNode(1) 
myTree.addNode(2) 
myTree.addNode(3) 
myTree.addNode(4) 
myTree.addNode(5) 
myTree.addNode(6) 
myTree.addNode(7) 
myTree.addNode(8) 
myTree.addNode(9) 
myTree.addNode(10)
myTree.addNode(11) 
myTree.addNode(12)

print(myTree.maxDepth(myTree.root))
