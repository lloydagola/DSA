
'''
bubble sort implementation using a for loop

Big-O
    Time Complexity  :
    Space Complexity :
'''

unsorted_listay = [64,34,25,12,22,11,90,5]

def bubble_sort(list, order = "ascending"):
    n = len(list)

    "ascending order"
    def asc():
        if list[j] > list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]

    def desc():
         if list[j] < list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]

    for i in range(n - 1) :
        for j in range(n - 1 - i) :
            if order == "descending":
                 desc()
            else:
                asc()

    return list

print(bubble_sort(unsorted_listay, "ascending"))