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
    
    def detectCycle(self):
        if self.head is None:
            return 0
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                counter = 1
                slow = slow.next
                while slow != fast:
                    counter += 1
                    slow = slow.next
                return counter
        return 0

        
        
            
  
myList = LinkedList()
for i in range(1, 10):
    myList.insertNode(i)

# Cycle: 9 -> 5
temp = myList.head
while temp.next is not None:
    temp = temp.next

fifth = myList.head
for _ in range(4):   # 5. düğüme git
    fifth = fifth.next

temp.next = fifth    # cycle oluştur

print(myList.detectCycle())  # True döner
