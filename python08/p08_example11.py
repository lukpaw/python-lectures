def is_leap_year(year):
    """
    Determines if a given year is a leap year.
    """

    # Check for divisibility by 400 first (most specific case)
    if year % 400 == 0:
        return True

    # Check for divisibility by 4 but not by 100 (remaining cases)
    if year % 4 == 0 and year % 100 != 0:
        return True

    return False  # Not a leap year if none of the above conditions are met


def days_in_month(year, month):
    """
    Calculates the number of days in a given month for a year.
    """

    # Validate month input (1-12)
    if month < 1 or month > 12:
        return None

    # Days in each month (excluding February)
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Handle February considering leap year
    if month == 2:
        days = days_in_months[1]  # Base case: 28 days
        if is_leap_year(year):
            days += 1  # Add 1 day for leap year

    else:
        # For other months, use the pre-defined list
        days = days_in_months[month - 1]

    return days


# Test data and expected results
test_years = [1900, 2000, 2016, 1987, 2024, 2024]  # Added more test cases
test_months = [2, 2, 1, 11, 2, 6]
test_results = [28, 29, 31, 30, 29, 30]  # Updated expected results

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result is None:
        print("Invalid month!")
    else:
        print(result, end=" ")
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")
