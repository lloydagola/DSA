'''
Binary Search implementation
Time Complexity: O(log n)
Space Complexity: O(1)
'''

def binarySearch(ls, low, high, query):
    print("binarySearch")
    while low <= high:
        mid = low + (high-low) // 2
        if query == ls[mid]:
            return mid        
        elif query < ls[mid]:
            high = mid - 1
        else:
            low = mid + 1        
    return -1


arr = [2, 3, 4, 10, 40]
query = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, query)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")