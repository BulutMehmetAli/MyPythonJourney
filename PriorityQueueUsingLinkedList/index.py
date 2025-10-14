class Node:
    def __init__(self , data , priority):
        self.data = data
        self.priority = priority
        self.next = None

class LinkedListPriority:

    def __init__(self):
        self.head = None
    
    def push(self , data , priority):
        newNode = Node(data , priority)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        if newNode.priority < temp.priority:
            newNode.next = temp
            self.head = newNode
            return
        while temp.next is not None and temp.next.priority < newNode.priority:
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

    def pop(self):
        if self.head is not None:
            temp = self.head 
            self.head = temp.next
            del temp
        else:
            raise ValueError('Head is NONE !!!')

    def peek(self):
        return self.head.data

pri = LinkedListPriority()

pri.push(10,3)
pri.push(5,6)
pri.push(1,4)
pri.push(7,9)
print(pri.peek())