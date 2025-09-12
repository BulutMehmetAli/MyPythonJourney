from collections import deque

class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
        nextRight = None
    
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

    def bfs(self , node):
        if node is None:
            return
        myQueue = deque()
        myQueue.append(node)
        mylist = []
        while myQueue:
            lvlSize = len(myQueue)
            lvlList = []
            for _ in range(lvlSize):
                temp = myQueue.popleft()
                lvlList.append(temp.data)
                if temp.left:
                    myQueue.append(temp.left)
                if temp.right:
                    myQueue.append(temp.right)
            mylist.append(lvlList)
        
        return mylist

    def connectRight(self , node):
        if node is None:
            return
        q = deque([node])

        while q:
            size = len(q)
            prev = None
            for _ in range(size):
                temp = q.popleft()
                if prev:
                    prev.nextRight = temp   # ✅ bağlantı yap
                prev = temp                 # ✅ prev güncelle
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            prev.nextRight = None           # ✅ seviyenin sonunu None yap

    def displayNextPointers(self , root):
        if not root:
            return
        
        q = deque([root])
        level = 0
        
        while q:
            size = len(q)
            level += 1
            node = q[0]   # o seviyedeki ilk düğüm
            print(f"Level {level}: ", end="")
            
            # nextRight pointerları takip et
            while node:
                print(node.data, end=" -> ")
                node = node.nextRight
            print("None")
            
            # sıradaki seviye için normal BFS ekle
            for _ in range(size):
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
    
    def debug(self , root):
        if not root:
            return
        
        q = deque([root])
        level = 0
        
        while q:
            size = len(q)
            level += 1
            print(f"\n--- Level {level} ---")
            print("Queue başlangıç:", [n.data for n in q])

            node = q[0]   # o seviyedeki ilk düğüm
            print(f"Level {level}: ", end="")
            
            # nextRight pointerları takip et
            while node:
                print(node.data, end=" -> ")
                node = node.nextRight
            print("None")
            
            # sıradaki seviye için normal BFS ekle
            for _ in range(size):
                temp = q.popleft()
                print(f"Popleft: {temp.data}")
                if temp.left:
                    q.append(temp.left)
                    print(f"Append left: {temp.left.data}")
                if temp.right:
                    q.append(temp.right)
                    print(f"Append right: {temp.right.data}")
            
            print("Queue seviye sonu:", [n.data for n in q])


# --- Test ---
myTree = Tree() 
for i in range(1, 13):
    myTree.addNode(i)

myTree.connectRight(myTree.root)
myTree.debug(myTree.root)