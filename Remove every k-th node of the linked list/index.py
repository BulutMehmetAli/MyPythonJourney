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
    
    def remKth(self , location):
        if self.head is None or location <= 0:
            return False
        
        if location == 1:
            self.head = None
            return True
        
        temp = self.head
        counter = 1
        while temp is not None:
            if (counter +1) % location == 0:
                temp.next = temp.next.next
            else:
                print(temp.data , end= " -> ")
                temp = temp.next
            counter += 1
        print("None")
        

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

myList.remKth(3)

