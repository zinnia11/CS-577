'''
Implement the optimal algorithm for inversion counting in either C, C++, C#, Java, Python, or Rust.
Be efficient and implement it in O(n log n) time, where n is the number of elements in the ranking.

The input will start with an positive integer, giving the number of instances that follow. 
For each instance, there will be a positive integer, giving the number of elements in the ranking. 

A sample input is the following:
2
5
5 4 3 2 1
4
1 5 9 8
The sample input has two instances. 
The first instance has 5 elements and the second has 4. 
For each instance, your program should output the number of inversions on a separate line. 
The correct output to the sample input would be:
10
1
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
def inversion_count(array):
    if len(array) == 1: return array, 0
    #left half
    A1, c1 = inversion_count(array[:len(array)//2])
    #right half
    A2, c2 = inversion_count(array[len(array)//2:])
    A, c = merge_count(A1, A2)
    return A, c+c1+c2

#main method to parse input
if __name__ == "__main__":
    #empty list
    array = []
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
            #split a line into individual nodes
            array = next(sys.stdin).split()
            array = [int(i) for i in array]
            #run inversion_count
            A, count = inversion_count(array)
            print(count)
            #finished with one instance
            num_instances-=1

