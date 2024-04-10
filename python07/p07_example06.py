# Days of the Week Representation
import calendar

# Monday is 0, Sunday is 6
print(calendar.MONDAY)  # Output: 0
print(calendar.SUNDAY)  # Output: 6

# Displaying a Yearly Calendar
import calendar

year_calendar = calendar.calendar(2025)
print(year_calendar)

# Displaying a Monthly Calendar
import calendar

month_calendar = calendar.month(2024, 10)  # October 2024
print(month_calendar)

# Changing the First Day of the Week
import calendar

calendar.setfirstweekday(6)  # Set Saturday as the first day
print(calendar.calendar(2024))

# Weekday Calculation
import calendar

day_of_week = calendar.weekday(2024, 4, 10)  # Wednesday (index 3)
print(day_of_week)

# Week Header Customization
import calendar

week_header = calendar.weekheader(3)  # Maximum 3 characters per day
print(week_header)  # Output: "Mon Tue Wed Thu Fri Sat Sun"

# Leap Year Check
import calendar

is_leap_year = calendar.isleap(2024)
print(is_leap_year)  # Output: False

# Custom Calendar Object
import calendar

custom_calendar = calendar.Calendar(6)  # Saturday as first day
for day in custom_calendar.iterweekdays():
    print(day, end=" ")  # Output: 6 0 1 2 3 4 5
