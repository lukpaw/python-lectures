from datetime import datetime, timedelta as tdel

# Get today's date and calculate tomorrow's date
today = datetime.today()
tomorrow = today + tdel(days=1)

# Print both dates in a formatted string
print(f"Today's date: {today:%B %d, %Y}")
print(f"Tomorrow's date: {tomorrow:%B %d, %Y}")
