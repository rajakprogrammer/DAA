#Find the sum of first N natural numbers using Iterative and Recursive algorithms. Find the time taken to execute the same by varying ‘N’s value and plot it using python’s plot function.
#Find the sum of first N natural numbers using Iterative and Recursive algorithms. Find the time taken to execute the same by varying ‘N’s value and plot it using python’s plot function.


import time
import matplotlib.pyplot as plt

# Iterative function to calculate the sum of first N natural numbers

def sum_iterative(N):
    result = 0
    for i in range(1, N + 1):
        result += i
    return result

 

# Recursive function to calculate the sum of first N natural numbers
def sum_recursive(N):
    if N == 1:
        return 1
    else:
        return N + sum_recursive(N - 1)

 

# Get user input for N
N = [10,800,650,799]
iterative=[]
recursive=[]
for i in N:
# Measure execution time for both methods
    start_time = time.time()
    iterative_sum = sum_iterative(i)
    end_time = time.time()
    iterative.append( end_time - start_time)

    start_time = time.time()
    recursive_sum = sum_recursive(i)
    end_time = time.time()
    recursive.append(end_time - start_time)

plt.figure(figsize=(10, 6))
plt.plot(N , recursive , marker='o' , label ='Execution Time Recursive' )
plt.plot(N , iterative , marker='o' , label ='Iterative Time Recursive' )
plt.xlabel('N')
plt.ylabel('Execution Time recursive')
plt.legend()
plt.grid(True)
plt.show()