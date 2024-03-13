def square_list(numbers):
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number * number)
    return squared_numbers


data = [1, 2, 3, 4]
squared_data = square_list(data)
print(squared_data)
