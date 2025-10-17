from collections import deque
import heapq

class Graph:
    
    def __init__(self , directed = False):
        self.directed = directed
        self.graphlist = dict()

    def add_node(self, node):
        if node not in self.graphlist:
            self.graphlist[node] = []
        else:
            raise ValueError(f"{node} already exists!")

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.graphlist:
            self.add_node(from_node)
        if to_node not in self.graphlist:
            self.add_node(to_node)

        # Ağırlık verilmediyse varsayılan 1 al
        if weight is None:
            weight = 1

        self.graphlist[from_node].append((to_node, weight))
        if not self.directed:
            self.graphlist[to_node].append((from_node, weight))
        
    def remove_node(self , node):
        if node not in self.graphlist:
            raise ValueError(f'{node} not exist !!!')
        for neighbor in self.graphlist:
            neighbor.discard(node)
        del self.graphlist[node]
    
    def remove_edge(self , from_node , to_node):
        if from_node in self.graphlist:
            if to_node in self.graphlist[from_node]:
                self.graphlist[from_node].remove(to_node)
            if not self.directed:
                if from_node in self.graphlist[to_node]:
                    self.graphlist[to_node].remove(from_node)
        raise ValueError('There is not any edge !!!')
    
    def get_neighbors(self , node):
        return self.graphlist.get(node , set())
    
    def has_node(self , node):
        return node in self.graphlist
    
    def has_edge(self , from_node , to_node):
        if from_node in self.graphlist:
            return to_node in self.graphlist[from_node]
        return False
    
    def get_nodes(self):
        return list(self.graphlist.keys())
    
    def get_edges(self):
        edges = []
        for from_node , neighbor in self.graphlist.items():
            for to_node in from_node:
                edges.append((from_node , to_node))
        return edges
    
    def get_node_edges(self , from_node):
        edges = []
        if from_node in self.graphlist:
            for to_node , _ in self.graphlist[from_node]:
                edges.append((from_node , to_node))
        return edges

    def bfs(self , startNode):
        visited = set()
        order = []
        queue = deque()
        queue.append(startNode)
        while queue:
            temp = queue.popleft()
            if temp not in visited:
                visited.add(temp)
                order.append(temp)
                neighbors = self.get_neighbors(temp)
                for neighbor in sorted(neighbors):
                    if isinstance(neighbor , tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order
    
    def dfs(self , startNode):
        visited = set()
        order = []
        stack = [startNode]
         
        while stack:
            temp = stack.pop()
            if temp not in visited:
                visited.add(temp)
                order.append(temp)
                neighbors = self.get_neighbors(temp)
                for neighbor in sorted(neighbors , reverse= True):
                    if isinstance(neighbor , tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order
    
    def shortest_path(self , from_node , to_node):
        visited = set()
        myQueue = deque()
        myQueue.append([from_node , [from_node]])
        while myQueue:
            node , path  = myQueue.popleft()
            if node == to_node:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor , _ in sorted(self.graphlist[node]):
                    if isinstance(neighbor , tuple):
                        neighbor = neighbor[0]
                    myQueue.append((neighbor , path + [neighbor]))
        return None


    def s_path(self , from_node , to_node):
        if from_node not in self.graphlist or to_node not in self.graphlist:
            raise ValueError('One or all are not exist !!!')
        visited = set()
        myQueue = deque()
        myQueue.append((from_node , [from_node]))
        while myQueue:
            node , path = myQueue.popleft()
            if node == to_node:
                return path
            if node not in visited:            
                visited.add(node)
                for neighbor , _ in self.graphlist[node]:
                    myQueue.append((neighbor , path + [neighbor]))

    def dijkstra(self , from_node):
        if from_node not in self.graphlist:
            raise ValueError("Node is not exist !!!")

        distances = {node: float('inf') for node in self.graphlist}
        distances[from_node] = 0
        visited = set()

        heap = [(0,from_node)]

        while heap:
            current_distance , current_node = heapq.heappop(heap)

            if current_distance > distances[current_node]:
                continue

            for neighbor , weight in self.graphlist[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap , (distance , neighbor))
        return distances  
    

    def dijks(self , from_node):
        if from_node not in self.graphlist:
            raise ValueError(f'{from_node} is not exist !!!')
        
        distances = {dist:float('inf') for dist in self.graphlist}
        distances[from_node] = 0
        visited = set()
        heap = [(0 , from_node)]

        while heap:
            current_node , current_distance = heapq.heappop(heap)

            if current_distance > distances[current_node]:
                continue
            """
            (5, 'A')
            (2, 'A')
            Burada 'A' düğümü iki kez heap’e eklendi:
            Biri 5 mesafesiyle (eski bilgi)
            Diğeri 2 mesafesiyle (güncel bilgi)
            Heap her zaman en küçük mesafeyi (2) önce çıkarır.
            Ama sonra 5 mesafeli olan çıkarsa, o zaten artık güncel değil.
            Bu yüzden o durumu atlamamız gerekir.
            """
            for neighbor , weight in self.graphlist:
                distance = distances[neighbor] + weight
                if current_distance > distance:
                    heapq.heappush(heap , (distance , neighbor))
        return distances
g = Graph(directed = False)

# Düğümleri ekleyelim
g.add_node('A')
g.add_node('B')


# Kenarları ekleyelim
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 1)
g.add_edge('A', 'E', 5)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 3)
g.add_edge('D', 'C', 4)
g.add_edge('D', 'G', 1)
g.add_edge('E', 'F', 1)
g.add_edge('G', 'F', 1)
g.add_edge('G', 'I', 2)
g.add_edge('I', 'D', 6)
g.add_edge('D', 'F', 1)

# Komşuları yazdıralım
for node in g.graphlist:
    print(f"{node}: {g.get_neighbors(node)}")

print("BFS ->", g.dfs('A'))

print(g.dijkstra('A'))
