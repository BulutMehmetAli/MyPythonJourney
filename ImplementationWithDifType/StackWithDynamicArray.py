# When using a fixed-size array, the stack has a maximum capacity that cannot grow beyond its 
# initial size. To overcome this limitation, we can use dynamic arrays. Dynamic arrays automatically 
# resize themselves as elements are added or removed, which makes the stack more flexible.

class DynamicStack:
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def popElement(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        return self.arr.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.arr[-1]

    def is_empty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)

    def __str__(self):
        return str(self.arr)

stack = DynamicStack()

stack.push(4)
stack.push(7)
stack.push(10)

print("Top:", stack.peek())
print("Pop:", stack.pop())
print("Size:", stack.size())
print("Stack:", stack)
