'''
Implement an algorithm to determine the maximum matching in a bipartite graph and if that matching
is perfect (all nodes are matched) in either C, C++, C#, Java, Python, or Rust. 
Be efficient and use your max-flow implementation from the previous week.

The input will start with an positive integer, giving the number of instances that follow. 
For each instance, there will be 3 positive integers m, n, and q. 
Numbers m and n are the number of nodes in node set A and node set B. 
Number q is the number of edges in the bipartite graph. 
For each edge, there will be 2 more positive integers i and j 
representing an edge between node 1 ≤ i ≤ m in A and node 1 ≤ i ≤ n in B.

For each instance, your program should output the size of the maximum matching, followed by a space,
followed by an N if the matching is not perfect and a Y if the matching is perfect. 
Each output line should be terminated by a newline. 
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


#graph instance, set A of nodes, and set B of nodes
def bipartite_matching(graph, A, B, numA, numB):
    #add a source
    for node in A:
        graph.add_edge('s', node, 1)
    #add a sink
    for node in B:
        graph.add_edge(node, 't', 1)

    #run max flow on the graph
    maxflow = graph.ford_fulkerson('s', 't') 

    if (numA != numB): #two sets don't have same num of nodes -> can't be perfect
        print(maxflow, "N")
    elif (numA != maxflow or numB != maxflow): #maxflow isn't same as num of nodes -> not perfect
        print(maxflow, "N")
    else: #perfect when maxflow == numA and numB
        print(maxflow, "Y")

    return


if __name__ == "__main__":
    g = Graph()
    setA = []
    setB = []
    #values to separate instances
    num_instances = int(next(sys.stdin))
    graph_info = next(sys.stdin).split() #list of num in set A, set B, and edges
    num_setA = int(graph_info[0])
    num_setB = int(graph_info[1])
    num_edges = int(graph_info[2])

    #taking standard input
    for line in sys.stdin:
        if (num_instances == 0):
            #no graphs left to parse, end
            break
        elif (num_edges == 0):
            #end of one instance, run bipartite_matching
            bipartite_matching(g, setA, setB, num_setA, num_setB)
            g = Graph()
            graph_info = line.split() #list of num in set A, set B, and edges
            num_setA = int(graph_info[0])
            num_setB = int(graph_info[1])
            num_edges = int(graph_info[2])
            num_instances-=1
        else:
            #split a line into individual nodes
            line_edge = line.strip().split()
            #start node, end node, capacity
            nodeA = line_edge[0]+'a'
            nodeB = line_edge[1]+'b'
            g.add_edge(nodeA, nodeB, 1) #for bipartite matching, all edges are capacity 1
            #store what nodes are in which set to add source and sink later
            if (nodeA not in setA):
                setA.append(nodeA)
            if (nodeB not in setB):
                setB.append(nodeB)
            #decrement number of edges left in a graph
            num_edges-=1

    #run bipartite_matching one more time
    bipartite_matching(g, setA, setB, num_setA, num_setB)

