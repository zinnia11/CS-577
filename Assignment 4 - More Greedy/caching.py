'''
For this question you will implement Furthest in the future paging in either C, C++, C#, Java, or
Python.

The input will start with an positive integer, giving the number of instances that follow. 
For each instance, the first line will be a positive integer, giving the number of pages in the cache. 
The second line of the instance will be a positive integer giving the number of page requests. 
The third and final line of each instance will be 
space delimited positive integers which will be the request sequence.

For each instance, your program should output the number of page faults achieved by furthest in the future 
paging assuming the cache is initially empty at the start of processing the page request sequence.
One output should be given per line. 

At the beginning, read the page requests and put the index of each in a dictionary with the 
page as the key. Then, when a page fault occurs, evict the page with the largest index and
delete all indices lower than it from the dictionary.
'''
import sys

def eviction(requests, cache):
    future =[]
    for p in cache:
        #no requests left for a page
        if (len(requests[p])==0):
            cache.remove(p)
            return
        #else append the next request for the page
        future.append((p,requests[p][0]))
    #remove the max index (aka furthest in the future) page
    cache.remove(max(future, key = lambda x:x[1])[0])

def furthest_future(pages, requests, cache_size):
    faults=0
    cache = []
    for p in pages:
        if p not in cache:
            #increment fault count
            faults += 1
            if len(cache)<cache_size:
                cache.append(p)
            else: #eviction
                eviction(requests, cache)
                cache.append(p)
        #pop the first index from the dictionary index list to maintain recency
        requests[p].pop(0)
                
    print(faults)

#main method to parse input
if __name__ == "__main__":
    #empty dictionary for storing page indices
    requests = {}
    #values to separate instances
    num_instances = int(next(sys.stdin))
    
    #taking standard input
    for line in sys.stdin:
        if (num_instances == 0):
            #no instances left to parse, end
            break
        else:
            num_size = int(line)
            num_requests = int(next(sys.stdin))
            #split a line into individual nodes and then put into the dictionary
            line_jobs = next(sys.stdin).split()
            #put each the index of the page request with the page number
            for i in range(num_requests):
                if line_jobs[i] in requests:
                    # append the new number to the existing array at this slot
                    requests[line_jobs[i]].append(i)
                else:
                    # create a new array in this slot
                    requests[line_jobs[i]] = [i]
            #end of one paging requests instance, run furthest_future
            furthest_future(line_jobs, requests, num_size)
            requests={}
            num_instances-=1