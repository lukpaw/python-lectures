def is_leap_year(year):
    """Determines if a given year is a leap year.

    Args:
        year: The year to check (integer).

    Returns:
        True if the year is a leap year, False otherwise.
    """

    # Check for divisibility by 400 first (most specific case)
    if year % 400 == 0:
        return True

    # Check for divisibility by 4 but not by 100 (remaining cases)
    if year % 4 == 0 and year % 100 != 0:
        return True

    return False  # Not a leap year if none of the above conditions are met


num_years = 5  # Number of years to check

# List to store valid years entered by the user
valid_years = []

for i in range(num_years):
    while len(valid_years) < i + 1:  # Loop until a valid year is entered
        year = int(input(f"Enter year {i + 1}: "))
        if year > 0:  # Check for positive year
            valid_years.append(year)  # Add valid year to the list

# Check leap years for valid years
for year in valid_years:
    result = is_leap_year(year)
    print(f"{year} -> {'Leap year' if result else 'Not a leap year'}")
