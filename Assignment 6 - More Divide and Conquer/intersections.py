'''
Suppose you are given two sets of n points, one set {p1, p2, . . . , pn} on the line y = 0 
and the other set {q1, q2, . . . , qn} on the line y = 1. 
Create a set of n line segments by connecting each point pi to the corresponding point qi. 

Your goal is to develop an algorithm to determine how many pairs of these line segments intersect. 
Your algorithm should take the 2n points as input, and return the number of intersections. 
Using divide-and-conquer, you should be able to develop an algorithm that runs in O(n log n) time.

Hint: What does this problem have in common with the problem of counting inversions in a list?

Input should be read in from stdin. 
The first line will be the number of instances. 
For each instance, the first line will contain the number of pairs of points (n). 
The next n lines each contain the location x of a point qi on the top line. 
Followed by the final n lines of the instance 
each containing the location x of the corresponding point pi on the bottom line. 
'''
import sys

def merge_count(left, right):
    sorted=[]
    count=0
    i = 0
    j = 0
    while(len(sorted) != len(left)+len(right)):
        if (i == len(left)):
            #no more elements in array1 (left half)
            sorted.extend(right[j:])
            break
        elif (j == len(right)):
            #no more elements in array2 (right half)
            sorted.extend(left[i:])
            break

        if (left[i]<=right[j]):
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
            # there is an inversion
            count+=len(left)-i

    return sorted, count

#while sorting the list, count number of inversions
def intersection_count(array):
    if len(array) == 1: return array, 0
    #left half
    A1, c1 = intersection_count(array[:len(array)//2])
    #right half
    A2, c2 = intersection_count(array[len(array)//2:])
    A, c = merge_count(A1, A2)
    return A, c+c1+c2

#main method to parse input
if __name__ == "__main__":
    #empty lists
    q = []
    p = []
    #values to separate instances
    num_instances = int(next(sys.stdin))
    
    #taking standard input
    for line in sys.stdin:
        if (num_instances == 0):
            #none left to parse, end
            break
        else:
            #elements in the list
            num_ele = int(line)
            #add all the points in each line
            q = [int(next(sys.stdin)) for i in range(num_ele)]
            p = [int(next(sys.stdin)) for i in range(num_ele)]
            #sort q and keep endpoints in p in the same order
            indices = sorted(range(len(q)), key=lambda i: q[i])
            p = [p[i] for i in indices]
            #run inversion_count to count inversions in the endpoints
            A, count = intersection_count(p)
            print(count)
            #finished with one instance
            num_instances-=1
