class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, val):
        self.stack_list.append(val)

    def pop(self):
        val = self.stack_list[-1]
        del self.stack_list[-1]
        return val


# Usage
stack_object = Stack()

print(len(stack_object.stack_list))  # Output: 0 (initial state)

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.stack_list)  # Output: [3, 2, 1]

print(stack_object.pop())  # Output: 1
print(stack_object.pop())  # Output: 2
print(stack_object.pop())  # Output: 3

print(stack_object.stack_list)  # Output: []
