import datetime

# Define a future event date (e.g., a birthday)
event_date = datetime.date(2024, 12, 31)

# Get the current date
current_date = datetime.date.today()

# Calculate the remaining days until the event
days_left = (event_date - current_date).days

# Display the result
print(f"Days left until the event: {days_left} days")
