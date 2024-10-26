'''
 Given an array of distinct integer values, count the number of pairs of integers that
 have difference k. For example, given the array { 1, 7, 5, 9, 2, 12, 3} and the difference
 k = 2,there are four pairs with difference2: (1, 3), (3, 5), (5, 7), (7, 9)
'''


'''
solution using set
'''
def count_pairs_with_difference(arr, k):
    count = 0
    value_set = set(arr)  # Step 2: Store all elements in a set
    
    for value in arr:  # Step 3: Loop through each element in the array
        if (value + k) in value_set:
            count += 1  # Increment count if value + k exists in the set
        if (value - k) in value_set:
            count += 1  # Increment count if value - k exists in the set
    
    return count // 2  # Step 4: Each pair is counted twice, so we divide by 2

# Example usage:
arr = [1, 7, 5, 9, 2, 12, 3]
k = 2
print(f"Number of pairs with difference {k}: {count_pairs_with_difference(arr, k)}")



'''
solution using hash tables
'''

def count_pairs_with_difference(arr, k):
    # Step 1: Create a hash table to store the elements of the array
    value_dict = {}
    count = 0

    # Step 2: Populate the hash table with the array elements
    for value in arr:
        value_dict[value] = True

    # Step 3: Loop through the array and check for pairs
    for value in arr:
        # Step 4: Check if value + k exists in the hash table
        if (value + k) in value_dict:
            count += 1
        # Step 5: Check if value - k exists in the hash table
        if (value - k) in value_dict:
            count += 1

    # Step 6: Each pair is counted twice, so we divide the count by 2
    return count // 2

# Example usage:
arr = [1, 7, 5, 9, 2, 12, 3]
k = 2
print(f"Number of pairs with difference {k}: {count_pairs_with_difference(arr, k)}")
