# Reading File Contents
# Example: Read the entire file
with open("data.txt", "r") as file:
    contents = file.read()
    print(contents)

# Example: Read one line at a time
with open("data.txt", "r") as file:
    line = file.readline()
    print(line)

# Example: Read all lines into a list
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Example: Read bytes into a bytearray
with open("image1.png", "rb") as file:
    image_data = bytearray(1024)
    file.readinto(image_data)
    # Process the bytearray data

# Example: Write text to a file
with open("output.txt", "w") as file:
    file.write("This is some new text data.")

# Example: Write bytearray data to a file
with open("image2.png", "wb") as file:
    image_data = bytearray(b" \xff\x00\x00")  # Example byte data
    file.write(image_data)

# Example: Print each line of a file
with open("data.txt", "r") as file:
    for line in file:
        print(line, end='')
