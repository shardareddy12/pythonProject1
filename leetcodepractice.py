
class Stack:
    def __init__(self):
        self.stack = []

    def size(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        if len(self.stack)==0:
            return True
        else:
            return False

    def push(self, num):
        return self.stack.append(num)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[self.size()-1]

    def display(self):
        print(self.stack)

my_stack = Stack()
my_stack.push(2)
my_stack.push(3)

print(my_stack.is_empty())
print(my_stack.peek())
my_stack.display()
