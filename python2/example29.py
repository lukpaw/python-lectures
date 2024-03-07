# Declare variables
x = 10  # 1010 in binary
y = 12  # 1100 in binary

# Bitwise operations
print(x & y)  # 8 (1000 in binary) - bitwise AND
print(x | y)  # 14 (1110 in binary) - bitwise OR
print(x ^ y)  # 6 (0110 in binary) - bitwise XOR
print(~x)  # -11 (1101 in binary, with 2's complement) - bitwise NOT

# Display binary representation
print(bin(x))  # 0b1010
print(bin(y))  # 0b1100

# Bitwise shift
print(x << 2)  # 40 (101000 in binary) - left shift by 2 bits
print(x >> 2)  # 2 (10 in binary) - right shift by 2 bits
