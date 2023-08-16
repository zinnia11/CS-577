'''
Implement the algorithm for the Knapsack Problem. 
Be efficient and implement it in O(nW ) time, where n is the number of items and W is the capacity.

The input will start with an positive integer, giving the number of instances that follow. 
For each instance, there will two positive integers, representing the number of items and the capacity, 
followed by a list describing the items. 
For each item, there will be two nonnegative integers, representing the weight and value, respectively.

For each instance, your program should output the maximum possible value.
'''
import sys

# i is last index of the list, w is max weight
# Bellman: = max{K(i − 1, w), K(i − 1, w − wi) + vi} for w ≥ wi
#            K(i − 1, w) for w < wi
def knapsack(W_cap, items):
    K = [[0 for x in range(W_cap + 1)] for x in range(len(items) + 1)]

    #build K[][] starting from 0 and row by row
    for i in range(len(items) + 1):
        for w in range(W_cap + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif (items[i-1][0] <= w): #not over weight limit
                K[i][w] = max(items[i-1][1]
                              + K[i-1][w-items[i-1][0]],
                              K[i-1][w])
            else: #over weight limit, meaning that part of Bellman is 0
                K[i][w] = K[i-1][w]
 
    print(K[len(items)][W_cap])

#main method to parse input
if __name__ == "__main__":
    #empty list for the jobs
    items = []
    #values to separate instances
    num_instances = int(next(sys.stdin))
    line = next(sys.stdin).split()
    num_items = int(line[0])
    weight_cap = int(line[1])
    
    #taking standard input
    for line in sys.stdin:
        if (num_instances == 0):
            #no graphs left to parse, end
            break
        elif (num_items == 0):
            #end of one instance, run finish_first
            knapsack(weight_cap, items)
            items=[]
            line = line.split()
            num_items = int(line[0])
            weight_cap = int(line[1])
            num_instances-=1
        else:
            #split a line into individual nodes and then put into the dictionary
            line = line.split()
            #weight, value
            items.append([int(line[0]), int(line[1])])
            #decrement number of items
            num_items-=1

    #run finish_first one more time
    knapsack(weight_cap, items)