class myStack:
    def __init__(self, cap):
        self.arr = [0] * cap
        self.capacity = cap
        self.top = -1
    
    def push(self, node):
        if self.isStackFull():
            print("Stack is Overflow")
            return
        
        self.top += 1
        self.arr[self.top] = node
        print(node, "is added")

    def pop(self):
        if self.isStackEmpty():
            print("Stack is Underflow")
            return None
        
        value = self.arr[self.top]
        self.top -= 1
        return value

    def topArr(self):
        if self.isStackEmpty():
            print("Stack is empty")
            return None
        return self.arr[self.top]

    def isStackEmpty(self):
        return self.top == -1

    def isStackFull(self):
        return self.top == self.capacity - 1

stack = myStack(10)

stack.push(4)
stack.push(6)
stack.push(9)
stack.push(4)
stack.push(2)
stack.push(1)
stack.push(1)
stack.push(1)


print("Popped:", stack.pop())
print("Top element:", stack.topArr())
print("Is full:", stack.isStackFull())
print("Is empty:", stack.isStackEmpty())