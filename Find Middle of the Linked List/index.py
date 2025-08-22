class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertNode(self , data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.next = None
    
    def sizeOfList(self , head):
        if self.head is None:
            return -1
        counter = 1
        temp = self.head
        while temp.next is not None:
            counter += 1
            temp = temp.next
        return counter
    
    def findMiddle(self):
        size = self.sizeOfList(self.head)
        if size == 1:
            return self.head
        temp = self.head
        s = size // 2
        counter = 0
        while temp is not None:
            temp = temp.next
            if s == 0 and counter == s:
                return temp.next
            elif s != 0 and counter == s-1:
                return temp.data
            counter += 1



        """elif size > 1 and size % 2 == 0 :
            temp = self.head
            s = (size / 2)-1
            while s >= 0:
                s -= 1
                temp = temp.next
            return temp.data
        elif size > 1 and size % 2 != 0:
            temp = self.head
            size = (size / 2)-1
            while size > 0:
                size-=1
                temp = temp.next
            return temp.data"""


           

myList = LinkedList()

myList.insertNode(1)
myList.insertNode(2)
myList.insertNode(3)
myList.insertNode(4)
myList.insertNode(5)
myList.insertNode(6)
myList.insertNode(7)
myList.insertNode(8)
myList.insertNode(9)

print(myList.findMiddle())
