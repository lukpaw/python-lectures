stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]  # delete the last item
    return val


print(len(stack))  # Output: 0 (initial state)

push(3)
push(2)
push(1)

print(stack)  # Output: [3, 2, 1]

print(pop())  # Output: 1
print(pop())  # Output: 2
print(pop())  # Output: 3

print(stack)  # Output: []
