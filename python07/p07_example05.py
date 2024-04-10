# Creating a Date Object
from datetime import date

my_date = date(2024, 4, 10)  # Today's date
print("Year:", my_date.year)
print("Month:", my_date.month)
print("Day:", my_date.day)


# Getting Today's Date
from datetime import date

today = date.today()
print("Today:", today)


# Dates from Timestamps
from datetime import date
import time

timestamp = time.time()
date_from_timestamp = date.fromtimestamp(timestamp)
print("Date from timestamp:", date_from_timestamp)


# Creating Time Objects
from datetime import time

specific_time = time(10, 30, 25)
print("Hour:", specific_time.hour)
print("Minute:", specific_time.minute)
print("Second:", specific_time.second)


# Sleeping for a Duration
import time

time.sleep(2)  # Wait for 2 seconds
print("Hello world!")


# Combining Dates and Times
from datetime import datetime

combined_datetime = datetime(2024, 4, 10, 14, 34)
print("Datetime:", combined_datetime)


# Formatting Dates and Times
from datetime import datetime

now = datetime.now()
formatted_datetime = now.strftime("%A, %B %d, %Y")  # Thursday, April 10, 2024
print(formatted_datetime)


# Date and Time Calculations
from datetime import date

date1 = date(2025, 1, 1)
date2 = date(2024, 1, 1)

difference = date1 - date2
print(difference)  # 366 days, 0:00:00

# timedelta objects can be used in calculations (e.g., multiplied by a number)
date_in_a_year = difference * 2
print(date_in_a_year)  # 732 days, 0:00:00