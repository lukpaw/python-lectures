def my_function():
    print(f"Running my_function from {__name__}")


if __name__ == "__main__":
    # Code to be executed only when the module is run directly
    print("Running the module directly")
    my_function()
