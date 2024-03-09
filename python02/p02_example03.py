# While loop
i = 0
while i < 3:
    print(f"Value of i in the while loop: {i}")
    i += 1

# For loop
for i in range(3):
    print(f"Value of i in the for loop: {i}")

# Break statement
for i in range(10):
    if i == 5:
        print("Breaking the for loop with break statement")
        break

# Continue statement
for i in range(10):
    if i % 4 == 0:
        print(f"Skipping iteration for i = {i}")
        continue
