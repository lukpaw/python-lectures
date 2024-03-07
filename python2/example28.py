# Create a 2D list (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access elements
print(matrix[0][1])  # Output: 2
print(matrix[2][2])  # Output: 9

# Iterate over the 2D list
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Add a new row to the 2D list
matrix.append([10, 11, 12])

# Remove a row from the 2D list
matrix.pop()

# Get the dimensions of the 2D list
len(matrix), len(matrix[0])

# Transpose the 2D list
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]


# Multiply two 2D lists (matrices)
# Assuming the matrices are compatible for multiplication
def matrix_multiplication(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


# Print the 2D list
print(matrix)
