# Dictionary: Phonebook example

phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

# Search for a contact
search_name = input("Enter a name to search: ")

if search_name in phonebook:
    number = phonebook[search_name]
    print(f"{search_name}'s number is: {number}")
else:
    print(f"{search_name} not found in the phonebook.")

# Add a new contact
new_name = input("Enter a new name: ")
new_number = input(f"Enter the phone number for {new_name}: ")
phonebook[new_name] = new_number
print(f"{new_name} has been added to the phonebook.")

# Print the entire phonebook
print("\nPhonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")
