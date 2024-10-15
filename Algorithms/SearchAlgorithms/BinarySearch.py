'''
Binary Search implementation
Time Complexity: O(log n)
Space Complexity: O(1)
'''

def binarySearch(ls, low, high, x):
    print("binarySearch")
    while low <= high:
        mid = low + (high-low) // 2

        if x == ls[mid]:
            return mid
        
        elif x < ls[mid]:
            high = mid - 1

        else:
            low = mid + 1        
    return -1


arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")