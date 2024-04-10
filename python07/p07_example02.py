# Lambda Functions
# Regular function
def square(x):
    return x * x


# Lambda function
lambda_square = lambda x: x * x

# Usage
print(square(5))  # Output: 25
print(lambda_square(5))  # Output: 25

# The map() Function
short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)  # Output: ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor']

# The filter() Function
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)  # Output: ['Python', 'Monty']


# Closures
def tag(tg):
    tg2 = tg  # Create a copy
    tg2 = tg[0] + '/' + tg[1:]  # Modify the copy

    def inner(str):
        return tg + str + tg2

    return inner  # Return the inner function


b_tag = tag('<b>')
print(b_tag('Monty Python'))  # Output: <b>Monty Python</b>
