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
    
    def remove(self , value):

        if self.head == None:
            return False
        
        while self.head and self.head.data == value:
            self.head = self.head.next
            
        temp2 = self.head
        while temp2 and temp2.next:
            if temp2.next.data == value:
                temp2.next = temp2.next.next
            else:
                temp2 = temp2.next
        
        return True
     
    def displayList(self): 
        if self.head == None: 
            return False 
        temp = self.head 
        while temp: 
            print(temp.data , end= " -> ") 
            temp = temp.next 
        print("None")

myList = LinkedList()

myList.insertNode(1)
myList.insertNode(2)
myList.insertNode(3)
myList.insertNode(1)
myList.insertNode(5)
myList.insertNode(6)
myList.insertNode(1)
myList.insertNode(8)
myList.insertNode(9)
myList.insertNode(18)
myList.insertNode(99)

myList.remove(1)
myList.displayList()

