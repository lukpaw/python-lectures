import math  # Import math library for square root calculation


def is_prime(num):
    """
    Checks if a number is prime.
    """

    # Handle cases for 1 and less (not prime) and 2 (prime)
    if num <= 1:
        return False
    if num == 2:
        return True

    # Check for divisibility only up to the square root of num (efficient)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    # If no divisors found, the number is prime
    return True


# Print prime numbers from 1 to 19
for i in range(1, 20):
    if is_prime(i):
        print(i, end=" ")
print()
