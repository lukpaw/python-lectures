def create_seating_chart():
    """
    Creates a two-dimensional list representing a seating chart.
    """
    seating_chart = [
        ["John", "Emily", "Michael"],
        ["Sarah", "William", None],
        ["Olivia", None, "Daniel"]
    ]
    return seating_chart


def print_seating_chart(chart):
    """
    Prints the seating chart with row numbers and seat occupancy.
    """
    for row_index, row in enumerate(chart):
        print(f"Row {row_index + 1}:", end=" ")
        for seat in row:
            if seat is None:
                print("Empty", end=" ")
            else:
                print(seat, end=" ")
        print()


def update_seat(chart, row, col, name):
    """
    Updates a seat in the seating chart with a given name.
    """
    if 0 <= row < len(chart) and 0 <= col < len(chart[row]):
        chart[row][col] = name
    else:
        print("Invalid row or column index!")


# Create the seating chart
seating_chart = create_seating_chart()

# Print the initial chart
print("Initial Seating Chart:")
print_seating_chart(seating_chart)

# Update a seat
update_seat(seating_chart, 1, 1, "David")

# Print the updated chart
print("\nUpdated Seating Chart:")
print_seating_chart(seating_chart)
