 def inOrder(self , node):
        if self.root == None: 
            return False 
        self.inOrder(node.left) 
        print(node.data , " -> ") 
        self.inOrder(node.right)
