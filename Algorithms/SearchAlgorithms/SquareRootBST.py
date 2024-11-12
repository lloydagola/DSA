class SquareRoot:
    def calculateSquareRoot(_, num):
        low, high = 0, num // 2

        while low <= high:
            mid = (low + high) // 2
            mid_squared = mid * mid

            if mid_squared == num:
                return mid
            elif mid_squared > num:
                high = mid - 1
            elif mid_squared < num:
                low = mid + 1
    
    
squareRoot = SquareRoot()
print(squareRoot.calculateSquareRoot(64))
    