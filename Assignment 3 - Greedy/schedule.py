'''
Algorithm for interval scheduling: Finish First
Sort requests in O(nlogn) time. 
Loop through sorted list and schedule each one in order with no conflicts. 
(If start time is later than the current scheduled finish time, then schedule that job)

The input will start with an positive integer, giving the number of instances that follow. 
For each instance, there will be a positive integer, giving the number of jobs. 
For each job, there will be a pair of positive integers i and j, 
where i < j, and i is the start time, and j is the end time.

For each instance, your program should output the number of intervals scheduled on a separate line.
Each output line should be terminated by a newline.
'''
import sys

def finish_first(jobs):
    #sort by finish time, aka second index of ordered pair
    jobs.sort(key = lambda x: x[1])
    #time to compare to for no conflicts
    start = jobs[0][1]
    total = 1

    #go through all of the jobs by finish time and schedule non-conflicting ones
    for job in jobs[1:]:
        if (job[0]>=start):
            total += 1
            start = job[1]

    print(total)       

#main method to parse input
if __name__ == "__main__":
    #empty list for the jobs
    jobs = []
    #values to separate instances
    num_instances = int(next(sys.stdin))
    num_jobs = int(next(sys.stdin))
    
    #taking standard input
    for line in sys.stdin:
        if (num_instances == 0):
            #no graphs left to parse, end
            break
        elif (num_jobs == 0):
            #end of one instance, run finish_first
            finish_first(jobs)
            jobs=[]
            num_jobs = int(line.strip())
            num_instances-=1
        else:
            #split a line into individual nodes and then put into the dictionary
            line_times = line.split()
            jobs.append([int(line_times[0]), int(line_times[1])])
            #decrement number of nodes left in a graph and then number of graphs left
            num_jobs-=1

    #run finish_first one more time
    finish_first(jobs)
