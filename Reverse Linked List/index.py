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
    
    def reverseList(self, head):
        prev = None
        current = head
        while current is not None:
            nxt = current.next   
            current.next = prev  
            prev = current       
            current = nxt        
        self.head = prev             
        
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
myList.insertNode(4)
myList.insertNode(5)
myList.insertNode(6)
myList.insertNode(7)
myList.insertNode(8)
myList.insertNode(9)

myList.reverseList(myList.head)
myList.displayList()