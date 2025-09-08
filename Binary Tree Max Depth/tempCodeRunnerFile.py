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
                if node.left:
                    myQueue.append(node.left)
                if node.right:
                    myQueue.append(node.right)
            mylist.append(lvlList)
        
        return mylist