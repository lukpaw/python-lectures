def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:  # Catch any other unexpected exceptions
        print(f"An error occurred while reading the file: {e}")
    return None



# file_content = read_file("./data2.txt")
# file_content = read_file("./data.jpeg")
file_content = read_file("./data.txt")

if file_content:
    print("File contents:")
    print(file_content)
else:
    print("Failed to read the file.")
