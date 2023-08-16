"""
Input: 
The first line contains an integer t, indicating the number of instances that follows. 
For each instance, the first line contains an integer n, indicating the number of nodes in the graph. 
Each of the following n lines contains several space-separated strings, 
where the first string s represents the name of a node, 
and the following strings represent the names of nodes that are adjacent to node s. 
You canassume that the nodes are listed line-by-line in lexicographic order (0-9, then A-Z, then a-z), 
and the adjacent nodes of a node are listed in lexicographic order. 
For example, consider two consecutive lines of an instance:
0, F
B, C, a
Note that 0 < B and C < a.

First line: t, number of graphs
Second line/first line of each instance: n, number of nodes
Following n lines: each line is a node, so each graph has n lines 
Each line: adjacency list

Input constraints:
•1 ≤t ≤1000
•1 ≤n ≤100
•Strings only contain alphanumeric characters
•Strings are guaranteed to be the names of the nodes in the graph.

Output: 
For each instance, print the names of nodes visited in depth-first traversal of the graph, 
with ties between nodes visiting the first node in input order. 
Start your traversal with the first node in input order. 
The names of nodes should be space-separated, and each line should be terminated by a newline.
"""
import sys

def DFS_helper(graph, node, visited, traversal):
    # add to visited and print the next visited node
    visited.add(node)
    traversal.append(node)

    for n in graph[node]:
        if (n not in visited):
            DFS_helper(graph, n, visited, traversal)

#simple DFS algorithm
#graph is a dictionary where the key is the node and the values are the adjacent nodes
#visited is a set of already visited nodes
def DFS(graph, visited):
    #loop through entire dictionary
    traversal=[]

    for node in graph:
        if (node not in visited):
            DFS_helper(graph, node, visited, traversal)

    print(' '.join((i for i in traversal)))


#main method to parse input
if __name__ == "__main__":
    #empty dictionary for the graph
    graph = {}
    visited=set()
    #values to separate instances
    num_graphs = int(next(sys.stdin))
    num_nodes = int(next(sys.stdin))
    
    #taking standard input
    for line in sys.stdin:
        if (num_graphs == 0):
            #no graphs left to parse, end
            break
        elif (num_nodes == 0):
            #end of one graph instance, run DFS
            DFS(graph, visited) #dict is ordered so first element is first input
            graph={}
            visited=set()
            num_nodes = int(line.strip())
            num_graphs-=1
        else:
            #split a line into individual nodes and then put into the dictionary
            line_nodes = line.split()
            graph.update({line_nodes[0]:line_nodes[1:]})
            #decrement number of nodes left in a graph and then number of graphs left
            num_nodes-=1

    #DFS on the last graph
    DFS(graph, visited) 