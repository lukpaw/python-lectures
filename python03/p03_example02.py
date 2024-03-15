print("--- Greet ---")


def greet(name="Anonymous"):
    print("Hello", end="")
    if name == "Anonymous":
        print()
        return
    print(f" {name}")
    return  # Optional return here


greet("James")
greet()

print("--- Greet 2 ---")


def greet2(name=None):
    print("Hello", end="")
    if name is None:
        print()
        return
    print(f" {name}", end="")
    print()
    return  # Optional return here


greet2("James")
greet2()
