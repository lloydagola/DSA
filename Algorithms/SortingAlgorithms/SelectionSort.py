
'''
Selection sort implementation using nested for loop
Big-P
    Time Complexity  : quadratic O(n^2)
    Space Complexity : constant O(1)
'''

unsorted_list = [64,34,25,12,22,11,90,5]

def selection_sort(ls):
    n = len(ls)

    if n <= 1:
        return ls
    
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if ls[j] < ls[min_index]:
                min_index = j

        ls[i], ls[min_index] = ls[min_index], ls[i]

    return ls

print(selection_sort(unsorted_list))