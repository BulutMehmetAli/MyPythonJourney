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
    
    def countList(self , numb):
        counter = 0
        temp = self.head
        while temp:
            if temp.data == numb:
                counter += 1
            temp = temp.next
        return counter
    
    def rec(self, numb, init):

        if init is None:
            return 0
        
        if init.data == numb:
            return 1 + self.rec(numb, init.next)
        else:
            return self.rec(numb, init.next)

        
myList = LinkedList()

myList.insertNode(1)
myList.insertNode(2)
myList.insertNode(1)
myList.insertNode(4)
myList.insertNode(1)
myList.insertNode(6)
myList.insertNode(7)
myList.insertNode(1)
myList.insertNode(9)

print(myList.countList(6))