from typing import Dict, Set, Hashable, Iterable, Tuple
from collections import deque

class Graph:
    
    def __init__(self , directed = False):
        self.directed = directed
        self.adj_list = dict()
    
    def __repr__(self):  
        graph_str = ""
        for node , neighbors in self.adj_list.items():
            graph_str += f"{node} -> {neighbors}\n"
        return graph_str

    def add_node(self , node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node exist already")

    def remove_node(self , node):
        if node not in self.adj_list:
            raise ValueError("Node does not exist")
        
        for neighbors in self.adj_list.values():
            neighbors.discard(node)
        
        del self.adj_list[node]

    def add_edge(self , from_node , to_node , weight = None):
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)
        
        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node , weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node , weight))
    def remove_edge(self , from_node , to_node):
        if from_node in self.adj_list:
            if to_node in self.adj_list[from_node]:
                self.adj_list[from_node].remove(to_node)
            else:
                ValueError('Edge does not exist')
            if not self.directed:
                if from_node in self.adj_list[to_node]:
                    self.adj_list[to_node].remove(from_node)
        else:
            raise ValueError('Edge does not exist')

    def get_neighbors(self , node):
        return self.adj_list.get(node , set())

    def has_node(self, node):
        return node in self.adj_list

    def has_edge(self , from_node , to_node):
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False
        

    def get_nodes(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        for from_node , neighbors in self.adj_list.items():
            for to_node in neighbors:
                edges.append((from_node , to_node))

    def bfs(self , start):
        if start not in self.adj_list:
            return False
        visited = set()
        order = []
        myQueue = deque()
        myQueue.append(start)

        while myQueue:
            node = myQueue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)
                for neighbor in sorted(neighbors):
                    if isinstance(neighbor , tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        myQueue.append(neighbor)     
                    """
                    neighbor = ('A', 5)  # burada 'A' ilk eleman
                    neighbor = neighbor[0]  # 'A' olarak kalacak
                    """       
        return order
    
    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []
        
        while stack:
            nodes = stack.pop()  # Son eklenen elemanı çıkar
            if nodes not in visited:
                visited.add(nodes)
                order.append(nodes)
                neighbors = self.get_neighbors(nodes)
                
                # Komşuları ters sırayla gezmek için
                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor , tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return order
        
    def shortestPath(self , from_node , to_node):
        if from_node not in self.adj_list or to_node not in self.adj_list:
            raise ValueError('One or Two node dont exist')

        distances = {node: float('inf') for node in self.graphList}
        distances[from_node] = 0
       
        parents = {node: None for node in self.graphList}

        visited = set()
        myQueue = deque([from_node])

        while myQueue:
            current = myQueue.popleft()

            if current == to_node:   # hedefe ulaştık
                break
    def bfs_shortest_path(self , from_node , to_node):
        visited = set()
        queue = deque([(from_node , [from_node])]) #Kuyruğun içinde düğüm + o düğüme kadar olan yol saklıyoruz.
        # Mesela (start, [start]) demek → “şu an start düğümündeyim, yolum sadece [start].”
        
        while queue:
            node , path = queue.popleft() #node  şu anda bulunduğumuz node ve path de yolumuz
            if node == to_node:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor , _ in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append((neighbor , path + [neighbor]))
        return None
    

    
g = Graph(directed = False)

# Düğümleri ekleyelim
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_node('I')

# Kenarları ekleyelim
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 1)
g.add_edge('D', 'C', 1)
g.add_edge('A', 'E', 1)
g.add_edge('E', 'F', 1)
g.add_edge('G', 'F', 1)
g.add_edge('G', 'I', 1)
g.add_edge('I', 'D', 1)

# Komşuları yazdıralım
for node in g.adj_list:
    print(f"{node}: {g.get_neighbors(node)}")

# BFS ve DFS'i çağır
print("BFS ->", g.bfs('A'))
print("DFS ->", g.dfs('A'))

print(g.bfs_shortest_path('A' , 'D'))
