class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __repr__(self):  # Liste yazdırılınca düzgün görünsün
        return f"({self.data}, p={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.priorityArr = []

    def enqueue(self, data, pri):
        # Aynı veri zaten varsa hata ver
        if any(node.data == data for node in self.priorityArr):
            raise ValueError('Data is already available !!!')

        newNode = Node(data, pri)
        self.priorityArr.append(newNode)
        self.priorityArr.sort(key=lambda x: x.priority)  # priority'e göre sırala

    def dequeue(self):
        if not self.priorityArr:
            raise ValueError('Queue is empty !!!')
        return self.priorityArr.pop(0)  # en küçük öncelikli elemanı çıkar

    def show(self):
        return self.priorityArr

    
myQueu = PriorityQueue()

myQueu.enqueue(7,9)
myQueu.enqueue(10,3)
myQueu.enqueue(5,6)
myQueu.enqueue(1,4)
myQueu.enqueue(8,0)

print(myQueu.show())
        
