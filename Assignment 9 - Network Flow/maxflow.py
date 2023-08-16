'''
Implement the Ford-Fulkerson method for finding maximum flow in graphs with only integer edge ca-
pacities, in either C, C++, C#, Java, or Python. 
Be efficient and implement it in O(mF) time, 
where m is the number of edges in the graph and F is the value of the maximum flow in the graph. 
We suggest using BFS or DFS to find augmenting paths. (You may be able to do better than this.)
The input will start with a positive integer, giving the number of instances that follow. 

For each instance, there will be two positive integers, 
indicating the number of nodes n = |V| in the graph and the number of edges |E| in the graph. 
Following this, there will be |E| additional lines describing the edges. 
Each edge line consists of 
a number indicating the source node, a number indicating the destination node, and a capacity. 
The nodes are not listed separately, but are numbered {1 . . . n}.
Your program should compute the maximum flow value from node 1 to node n in each given graph.
'''
import sys

class Graph:
    def __init__(self):
        self.nodes = {} 
    
    def add_node(self, name):
        self.nodes[name] = Node(name)

    #add edges in general
    def add_edge(self, u, v, capacity):
        #add node first
        if (u not in self.nodes):
            self.add_node(u)
        if (v not in self.nodes):
            self.add_node(v)
            
        start = self.nodes[u]
        end = self.nodes[v]
        #add the end node if it isn't already one of the children
        if end not in start.children and capacity > 0:
            start.children.append(end)

        #store the cost
        if v in start.costs:
            start.costs[v] += capacity
        else:
            start.costs[v] = capacity

    #update edges in a residual graph
    def edge_update(self, u, v, capacity):  
        start = self.nodes[u]
        end = self.nodes[v]
        #update nodes in residual
        if end not in start.children and capacity > 0:
            start.children.append(end)
        #capacity of 0 means edge/child can disappear
        elif end in start.children and capacity == 0:
            start.children.remove(end)

        #store the cost of the path
        start.costs[v] = capacity
    
    #doesn't work for some reason
    '''
    #iterative version of DFS
    def DFS(self,s,t):           
        visited = []
        path = []
        stack = []
 
        stack.append(self.nodes[s])
 
        while (len(stack)):
            # Pop a node from stack
            current = stack[-1]
            stack.pop()
            
            #reach dest, end DFS
            if current.name == t:
                path.append(current.name)
                return path

            #add to visited
            if current.name not in visited:
                path.append(current.name)
                visited.append(current.name)
                #push children onto stack
                for child in reversed(current.children):
                    if child.name not in visited:
                        stack.append(child)

        return []
    '''


    def DFS(self, s, t):
        Node.visited = set() #clear visited set
        path = self.nodes[s].find_path(t)

        return [i for i in reversed(path)]
    

    def ford_fulkerson(self, s, t):
        max = 0

        while True: 
            path = self.DFS(s, t)
            #while we can still find an augmenting path
            if len(path) == 0:
                break
            
            #find bottleneck
            bottleneck = float("Inf") 
            for i in range(len(path)-1):
                if self.nodes[path[i]].costs[path[i+1]] < bottleneck:
                    bottleneck = self.nodes[path[i]].costs[path[i+1]]
            
            #increase flow by bottleneck
            max += bottleneck

            #update capacities of the edges and reverse edges
            for j in range(len(path)-1):
                #capacity reduce by bottleneck
                w = self.nodes[path[j]].costs[path[j+1]]
                self.edge_update(path[j], path[j+1], w - bottleneck) 

                #flow edges increase by bottlenexk
                if path[j] in self.nodes[path[j+1]].costs:
                    reverse = bottleneck + self.nodes[path[j+1]].costs[path[j]]
                else:
                    reverse = bottleneck
                
                self.edge_update(path[j+1], path[j], reverse)

        return max


class Node:
    visited = set()

    def __init__(self, name):
        self.name = name
        self.children = []  #children node objects
        self.costs = {} #children names and edge costs


    def find_path(self, t): 
        if self.name in Node.visited:
            return []
        
        Node.visited.add(self.name)

        #reach destination
        if self.name == t:
            return [self.name]
        #run into node without children
        if len(self.children) == 0: 
            return []

        #recurse
        for child in self.children:
            path = child.find_path(t)
            if(len(path) > 0):
                path.append(self.name)
                return path
                
        return []


if __name__ == "__main__":
    g = Graph()
    #values to separate instances
    num_instances = int(next(sys.stdin))
    graph_info = next(sys.stdin).split()
    num_nodes = graph_info[0]
    num_edges = int(graph_info[1])

    #taking standard input
    for line in sys.stdin:
        if (num_instances == 0):
            #no graphs left to parse, end
            break
        elif (num_edges == 0):
            #end of one instance, run ford_fulkerson
            print(g.ford_fulkerson("1", num_nodes))  
            g = Graph()
            graph_info = line.split()
            num_nodes = graph_info[0]
            num_edges = int(graph_info[1])
            num_instances-=1
        else:
            #split a line into individual nodes
            line_edge = line.strip().split()
            #start node, end node, capacity
            g.add_edge(line_edge[0], line_edge[1], int(line_edge[2]))
            #decrement number of edges left in a graph
            num_edges-=1

    #run ford_fulkerson one more time
    print(g.ford_fulkerson("1", num_nodes))  

