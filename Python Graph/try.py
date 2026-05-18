class Graph:
    
    def __init__(self , directed = False):
        self.directed = directed
        self.adj_list = set()
    
    def add_node(self , node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError('Node is exist')
    
    def add_edge(self , from_node , to_node , weight):
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
            

    def remove_node(self , node):
        if node not in self.adj_list:
            raise ValueError('Node does not exist')
        for neighbors in self.adj_list.values(node):
            neighbors.discard(node)
        del self.adj_list[node]
