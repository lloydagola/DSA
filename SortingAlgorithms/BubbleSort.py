
'''
bubble sort implementation using a for loop

Big-O
    Time Complexity  : constant O(1)
    Space Complexity : quadratic O(n^2)
'''

unsorted_list = [64,34,25,12,22,11,90,5]

n = len(unsorted_listay)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if unsorted_listay[j] > unsorted_listay[j+1]:
            unsorted_listay[j], unsorted_listay[j+1] = unsorted_listay[j+1], unsorted_listay[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:", unsorted_listay)