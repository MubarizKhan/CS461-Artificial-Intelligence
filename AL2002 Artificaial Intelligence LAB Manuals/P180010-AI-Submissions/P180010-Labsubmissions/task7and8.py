from collections import deque
from queue import PriorityQueue
import pprint

class weightedGraph:
    def __init__(self):
        print('const')
        self.graph = {}
    
    def add_node(self, node):
        print('ds')
        if node in self.graph:
            raise ValueError('Node already exists')
        self.graph[node] = []
    
    def add_edge(self, source, destination,cost):
        if source not in self.graph or destination not in self.graph:
            raise ValueError('either source or destination not in graph')
        
        children = self.graph[source]
        if destination not in children:
            children.append((destination,cost))
            
    def get_neighbors(self,source):
        neighbors = []
        if source not in self.graph:
            raise ValueError('source not in graph')
        for i in self.graph[source]:
            neighbors.append(i[0])
        return neighbors
    
    def get_cost(self,source, destination):
        cost = 0
        if source not in self.graph or destination not in self.graph:
            raise ValueError('Source & Destination both not in graph')
        for i in range(0, len(self.graph[source])):
            if self.graph[source][i] == destination:
                cost = self.graph[i][1]
            print('this is cost')
            return cost
        

def greedyBFS(graph, source, destination):
    print('gbfs')
    visited_nodes = []
    que = PriorityQueue()
    que.put((0, source))
    minimum_cost = float('inf')
    total_cost = 0
    
    while que:
        print(que)
        cost, node = que.get()
        if node not in visited_nodes:
            visited_nodes.append(node)
            if node == destination:
                print(total_cost, node)
                return que 
            for i in graph.get_neighbors(node):
                if i not in visited_nodes:
                    cost = graph.get_cost(node, i)
                if cost < minimum_cost:
                    minimum_cost = cost
                    loc = i
            que.put((minimum_cost, loc))
            total_cost = total_cost + minimum_cost
        # print('end')
    return False

def heuristic(graph, node, parent):
    heuristic_S = 5
    heuristic_S1 = 7
    heuristic_S2 = 3
    heuristic_S3 = 3
    
    h_G = 0
    # f(n) = g{n} + h(n)
    if node == 'S':
        g_S = 0
        f_n = g_S + heuristic_S
        return f_n
    if node == 'S1':
        g_S1 = graph.get_cost('S', 'S1')
        f_n = heuristic_S1 + g_S1
        return f_n
    if node == 'S2':
        g_S2 = graph.get_cost('S', 'S2') 
        f_n = g_S2 + heuristic_S2 
        return f_n
    
    if node == 'S3':
        g_S3 = graph.get_cost('S', 'S3')
        f_n = g_S3 + heuristic_S3
        return f_n 
    
    if node == 'G':
        if parent == 'S1':
            g_G = graph.get_cost('S', 'S1') + graph.get_cost('S1', 'G')
            f_n = g_G + h_G  
            return f_n  
            
    if parent == 'S2':
        g_G = graph.get_cost('S', 'S2') + graph.get_cost('S2','G')
        f_n = g_G + h_G
        return f_n
    
    if parent == 'S3':
        g_G = graph.get_cost('S', 'S3') + graph.get_cost('S3', 'G')
        f_n = g_G + h_G
        return f_n
    
def Astar(graph, src, dest):
    que = deque()
    que.append(src)
    costs = []
    path = []
    parent = ''
    lst = []
    
    while que:
        min_cost = float('inf')
        for q in que:
            print('1 node,parent',q,'ho',parent)
            cost = heuristic(graph, q, parent)
            print('2 node,cost',q,cost)

            if cost < min_cost:
                min_cost = cost
                node = q
                
        if node == dest:
            return
        que.remove(node)
        
        print('Min:', node, min_cost)
        path.append(node)
        neighbors = graph.get_neighbors(node)
        for n in neighbors:
            print('4 n:', n)
            if n == 'G':
                if node == 'S1':
                    parent = 'S1'
                if node == 'S2':
                    parent = 'S2'
                if node == 'S3':
                    parent = 'S3'
            que.append(n)
        print('-----------, path')
    


w = weightedGraph()
w.add_node('S')
w.add_node('S1')
w.add_node('S2')
w.add_node('S3')
w.add_node('G')
w.add_edge('S','S1',1)
w.add_edge('S','S2',5)
w.add_edge('S','S3',15)
w.add_edge('S1','G',10)
w.add_edge('S2','G',5)
w.add_edge('S3','G',5)
Astar(w,'S1','G')

# print('hi')
g = weightedGraph()

g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_edge('A','B',12)
g.add_edge('A','C',2)
g.add_edge('B','D',7)
g.add_edge('C','D',4)
g.add_edge('C','G',1)
g.add_edge('D','G',2)
g.add_edge('F','A',1)
g.add_edge('F','G',5)
# pprint.pprint(g.g)

greedyBFS(g,'A','G')
        