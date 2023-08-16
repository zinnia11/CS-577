'''
Implement the optimal algorithm for Weighted Interval Scheduling (for a definition of the problem, see
the slides on Canvas) in either C, C++, C#, Java, Python, or Rust. 
Be efficient and implement it in O(n^2) time, where n is the number of jobs.

The objective of the problem is to determine a schedule of non-overlapping intervals with maximum
weight and to return this maximum weight. 
For each instance, your program should output the total weight of the intervals scheduled on a separate line. 

The input will start with an positive integer, giving the number of instances that follow. 
For each instance, there will be a positive integer, giving the number of jobs. 
For each job, there will be a trio of positive integers i, j and k, where i < j, and 
i is the start time, j is the end time, and k is the weight.

Notes:
• Endpoints are exclusive, so it is okay to include a job ending at time t and a job starting at time t
in the same schedule.
'''
import sys

#function to find the first job that has no conflict with the job at index i
def no_conflict(jobs, i):
    # Initialize 'lo' and 'hi' for Binary Search
    lo = 0
    hi = i - 1
 
    # Perform binary Search iteratively
    while lo <= hi:
        mid = (lo + hi) // 2
        if jobs[mid][1] <= jobs[i][0]:
            if jobs[mid + 1][1] <= jobs[i][0]:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1

    return -1

#dynamic program to find maximum weight that can be scheduled
def max_weight_schedule(jobs):
    #sort by finish time, aka second index of ordered pair
    jobs.sort(key = lambda x: x[1])
    #matrix to store weights, length is number of jobs
    M = [None] * (len(jobs)+1)
    M[0] = jobs[0][2]

    for j in range(1, len(jobs)):
        take = jobs[j][2]
        k = no_conflict(jobs, j)
        if k != -1:
            take += M[k]
        
        M[j] = max(take, M[j-1])

    print(M[len(jobs)-1])       

#main method to parse input
def main():
    #empty list for the jobs
    jobs = []
    #values to separate instances
    num_instances = int(next(sys.stdin))
    num_jobs = int(next(sys.stdin))
    
    #taking standard input
    for line in sys.stdin:
        if (num_instances == 0):
            #no left to parse, end
            break
        if (num_jobs == 0):
            #end of one instance, run finish_first
            max_weight_schedule(jobs)
            jobs=[]
            num_instances-=1
            num_jobs = int(line.strip())
        else:
            #split a line into individual nodes
            line_times = line.split()
            #start time, finish time, weight
            jobs.append([int(line_times[0]), int(line_times[1]), int(line_times[2])])
            #decrement number of jobs
            num_jobs-=1

    max_weight_schedule(jobs)

main()