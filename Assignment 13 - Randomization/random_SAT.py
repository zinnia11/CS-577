'''
Implement an algorithm which, given a MAX 3-SAT instance, produces an assignment which satisfies
at least 7/8 of the clauses, in either C, C++, C#, Java, or Python.
The input will start with a positive integer n giving the number of variables, 
then a positive integer m giving the number of clauses, 
and then m lines describing each clause. 
The description of the clause will have three integers x y z, 
where |x| encodes the variable number appearing in the first literal in the clause, 
the sign of x will be negative if and only if the literal is negated, 
and likewise for y and z to describe the two remaining literals in the clause.
For example, 3 -1 -4 corresponds to the clause x3 ∨ NOT(x1) ∨ NOT(x4). 

A sample input is the following:
10
5
-1 -2 -5
6 9 4
-9 -7 -8
2 -7 10
-1 3 -6

Your program should output an assignment which satisfies at least ⌊7/8⌋m clauses. 
Return n numbers in a line, using a ±1 encoding for each variable 
(the ith number should be 1 if xi is assigned TRUE, and -1 otherwise). 
The maximum possible number of satisfied clauses is 5, 
so your assignment should satisfy at least ⌊7/8 * 5⌋ = 4 clauses.

One possible correct output to the sample input would be:
-1 1 1 1 1 1 -1 1 1 1
'''
import random

#empty list for the jobs
clauses = []
#values to separate instances
num_vars = int(input())
num_clauses = int(input())
    
#taking standard input
for i in range(num_clauses):
    #split a line into individual nodes and then put into a list
    line_times = input().split()
    clauses.append([int(line_times[0]), int(line_times[1]), int(line_times[2])])

# random_SAT
num_sat = 0
# keep running until condition is satisfied
while(num_sat < int((7/8)*num_clauses)):
    num_sat = 0
    X = random.choices([-1, 1], k=num_vars)
    # evaluate clauses
    for c in clauses:
        vars = [X[abs(c[0])-1], X[abs(c[1])-1], X[abs(c[2])-1]]
        # clauses are OR, so only need one to be True
        if (c[0]*vars[0] > 0 or c[1]*vars[1] > 0 or c[2]*vars[2] > 0): 
            num_sat += 1

# format output
output = ""
for x in X:
    output += "1 " if x==1 else "-1 "
print(output[:-1])
