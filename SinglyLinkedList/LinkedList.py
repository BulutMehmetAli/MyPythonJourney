class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = newNode
        newNode.next = None

    def traverseList(self):
        current = self.head
        while current is not None:
            print(current.data , end = " -> ")
            current = current.next
        print("None")

    def recursiveTraverseList(self,head):
        if head is None:
            print("None")
            return
        print(head.data , end=" -> ")
        self.recursiveTraverseList(head.next)
    def isAvailable(self,data):
        temp = self.head
        while(temp.next is not None):
            if data == temp.data:
                return True
            temp = temp.next
        if data == temp.data:
            return True
        return False
    def recAvailable(self,node,data):
        if node is None:
            return False
        if node.data == data:
            return True
        return(self.recAvailable(node.next , data))
    def sizeOfLinkedList(self,head):
        temp = head
        counter = 0
        if head is None:
            return False
        while temp.next != None:
            counter += 1
            temp = temp.next
        if counter > 0:
            counter += 1
        return counter
    
    def addBeginInLinkedList(self , data):
        if self.head is None:
            self.addNode(data)
        newNode = Node(data)
        temp = self.head
        self.head = newNode
        newNode.next = temp
        del temp
    def insertAfterNode(self , data , location):
        if self.head is None:
            self.addNode(data)
        size = self.sizeOfLinkedList(self.head)
        if location > size:
            return -1
        newNode = Node(data)
        temp = self.head
        while(location > 0):
            temp = temp.next
            location -= 1
        newNode.next = temp.next
        temp.next = newNode

myList = SinglyLinkedList()
myList.addNode(10)
myList.addNode(20)
myList.addNode(30)
myList.addNode(40)
myList.addNode(50)
myList.addNode(60)
myList.addBeginInLinkedList(0)
myList.insertAfterNode(58,3)
myList.traverseList()
