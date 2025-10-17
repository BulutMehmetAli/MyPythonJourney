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


    def topologicalList(self):
        if self.adj_list is None:
            raise ValueError('Graph is empty !!!')
        visited = set()
        nodeList = self.get_nodes()
        indegree = {node : 0 for node in self.adj_list}

        # 1️⃣ Her düğümün indegree'ini hesapla
        for node in self.adj_list:
            for neighbor in self.adj_list[node]:
                if isinstance(neighbor, tuple):
                    neighbor = neighbor[0]
                indegree[neighbor] += 1

        queue =deque()
        queue = [u for u in indegree if indegree[u] == 0]
        order = []
        while queue:
            temp = queue.pop()
            order.append(temp)
            visited.add(temp)

            for neighbor in self.adj_list[temp]:
                if isinstance(neighbor, tuple):
                    neighbor = neighbor[0]
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0 and neighbor not in visited:
                    queue.append(neighbor)
        
        return order
            


myGraph = Graph(True)

myGraph.add_node('A')        
myGraph.add_node('B')
myGraph.add_node('C')
myGraph.add_node('D')
myGraph.add_node('E')
myGraph.add_node('F')

myGraph.add_edge('A','D',3)
myGraph.add_edge('A','C',2)
myGraph.add_edge('D','E',2)
myGraph.add_edge('E','F',4)
myGraph.add_edge('B','C',1)
myGraph.add_edge('B','F',3)


print(myGraph.kahnsAlgorithm())
    
   
        
    