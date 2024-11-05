class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add(self, value):
        self.items.append(value)

    def remove(self):
        if not self.is_empty():
            self.items.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return -1

    def __str__(self):
        return str(self.items)


my_stack = Stack()
my_stack.add(1)
my_stack.add(1)
val = my_stack.peek()
print(val)
my_stack.remove()
print(my_stack)
    