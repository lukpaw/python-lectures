word1 = "apple"
word2 = "banana"

# Equal comparison
if word1 == word2:
    print(f"{word1} and {word2} are equal.")
else:
    print(f"{word1} and {word2} are not equal.")

# Less than comparison
if word1 < word2:
    print(f"{word1} is alphabetically before {word2}.")
else:
    print(f"{word1} is alphabetically after {word2}.")

# Sorting
fruits = ["banana", "apple", "cherry"]
print(f"Fruits: {fruits}")

sorted_fruits = sorted(fruits)  # sorted_fruits will be ['apple', 'banana', 'cherry']
print(f"Sorted fruits: {sorted_fruits}")

reversed_fruits = sorted(fruits, reverse=True)  # reversed_fruits will be ['cherry', 'banana', 'apple']
print(f"Reversed fruits: {reversed_fruits}")
