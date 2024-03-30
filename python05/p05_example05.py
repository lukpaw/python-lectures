num = 42
string_num = str(num)  # string_num will be "42"
print("String num: " + string_num)

float_num = 3.14
string_float = str(float_num)  # string_float will be "3.14"
print("String float: " + string_float)

pi_string = "3.14159"
pi_float = float(pi_string)  # pi_float will be 3.14159
# print("Pi float: " + pi_float)
# print("Pi float: " + str(pi_float))
print(f"Pi float: {pi_float}")

value = "123"
# int_value = int(value)  # This will work if value is a valid integer
int_value = int(value)  # Assuming value always contains a valid integer
print(f"Int float: {int_value}")
