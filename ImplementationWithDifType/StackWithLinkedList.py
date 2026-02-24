class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:

    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.head is None:
            raise IndexError("Stack Underflow")

        value = self.head.data
        self.head = self.head.next
        self._size -= 1
        return value

    def peek(self):
        if self.head is None:
            return "Stack is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size
myStack = MyStack()

myStack.push(5)
myStack.push(51)
myStack.push(55)
myStack.pop()
myStack.push(65)
myStack.push(9)
print(myStack.peek())

print("Is empty:" , myStack.is_empty())