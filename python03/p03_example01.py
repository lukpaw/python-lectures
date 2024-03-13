def introduction(first_name, last_name="Anonymous", age=-1):
    print(f"Hello, my name is {first_name} {last_name}. ", end="")
    if age >= 0:
        print(f"I am {age} years old.\n")
    else:
        print("\n")


print("--- Positional parameter passing ---")
introduction("Luke", "Skywalker", 25)

print("--- Keyword argument passing ---")
introduction(last_name="Skywalker", first_name="Luke", age=25)

print("--- Mixing positional and keyword arguments ---")
introduction("Luke", age=25, last_name="Skywalker")

print("--- Default values ---")
introduction("James")
