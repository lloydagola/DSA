'''
Quicksort implementation
Time Complexity: Linear Logarithmic O(n log n)
Space Complexity: Logarithmic O(Log n)
'''

def partition(ls, low, high):
    pivot = ls[high]
    i = low - 1

    for j in range(low, high):
        if ls[j] <= pivot:
            i += 1
            ls[j], ls[high] = ls[high], ls[j]

    ls[i+1], ls[high] = ls[high], ls[i+1]
    return i+1

def quicksort(ls, low=0, high=None):
    if high is None:
        high = len(ls)-1

    if low < high:
        pivot_index = partition(ls, low, high)
        quicksort(ls, low, pivot_index-1)
        quicksort(ls, pivot_index+1, high)