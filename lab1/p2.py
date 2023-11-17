# Perform linear and binary searches for an array of 10000 elements. Use random function in Python to generate the 
# integer array elements in the range 1 to 1000. The search key is an input 
# given by the user. Plot the time taken by the algorithm for 5 different searches when executing the two algorithms

import random
import time
import matplotlib.pyplot as plt

# Function to perform a linear search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Function to perform a binary search (assuming the array is sorted)
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Generate a random array of 10,000 elements
array_size = 10000
array = [random.randint(1, 1000) for _ in range(array_size)]
array.sort()  # Sort the array for binary search

# Input 5 search keys from the user
search_keys = []
for i in range(5):
    search_key = int(input(f"Enter search key {i + 1} (1-1000): "))
    search_keys.append(search_key)

# Perform linear searches and measure execution times
linear_search_times = []
for search_key in search_keys:
    start_time = time.time()
    linear_search(array, search_key)
    end_time = time.time()
    linear_search_times.append(end_time - start_time)

# Perform binary searches and measure execution times
binary_search_times = []
for search_key in search_keys:
    start_time = time.time()
    binary_search(array, search_key)
    end_time = time.time()
    binary_search_times.append(end_time - start_time)

# Plot the execution times for linear search
plt.figure(figsize=(10, 6))
plt.plot(search_keys, linear_search_times, marker='o', label='Linear Search')
plt.xlabel('Search Key')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time for Linear Search')
plt.legend()
plt.grid(True)

# Plot the execution times for binary search
plt.figure(figsize=(10, 6))
plt.plot(search_keys, binary_search_times, marker='o', label='Binary Search')
plt.xlabel('Search Key')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time for Binary Search')
plt.legend()
plt.grid(True)

plt.show()
