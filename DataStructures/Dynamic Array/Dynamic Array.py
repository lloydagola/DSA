class DynamicArray:

    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.elements = [0] * capacity        


    def get(self, i: int) -> int:
        return self.elements[i]


    def set(self, i: int, n: int) -> None:
        self.elements[i] = n


    def pushback(self, n: int) -> None:
        
        if self.capacity == n:
            self.resize()

        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.elements[self.size]
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2

        new_arr = [0] * self.self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]

        self.elements = new_arr


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity

dynamic_array = DynamicArray(1)
dynamic_array.set(0, "zero")

print("dynamic_array", dynamic_array)

item = dynamic_array.get(0)
print(item)

first = dynamic_array.set(0, "first")
print(first)


'''
print("pushback")
print("resize")
print("getSize")
print("getCapacity")
'''