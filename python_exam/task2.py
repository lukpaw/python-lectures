"""
==========================
Task instructions:
==========================
This program changes text to lowercase and removes first names (from a predefined list) from an text.
Predefined list of first names:
"John", "Jane", "Michael", "Sarah", "David", "Jennifer", "Robert", "Elizabeth", "William", "Mary"

==========================
Example Output:
==========================
Enter the text: This is a sample text with names like John, Jane, and Michael. How about Sarah appearing later?
Modified Text: this is a sample text with names like , , and . how about  appearing later?
"""

names = ["John", "Jane", "Michael", "Sarah", "David", "Jennifer",
         "Robert", "Elizabeth", "William", "Mary"]


def remove_first_names(text, names):
    """
    Finds and removes first names from a given text, ignoring case.

    Args:
        text: The English text to search for names in. (str)
        names: A list of first names to remove. (list)

    Returns:
        The modified text with names removed. (str)
    """

    # Convert the text to lowercase for case-insensitive search
    lower_text = text.lower()

    # Iterate through the list of names
    for name in names:
        # Use string replacement with a case-insensitive flag 'i'
        lower_text = lower_text.replace(name.lower(), "")

    return lower_text


user_text = input("Enter the text: ")
modified_text = remove_first_names(user_text, names)
print("Modified Text:", modified_text)
