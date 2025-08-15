from logic import *
import csv

def update_csv_value(filename, row_index, column_header, new_value) -> None:
    """
    Updates a specific value in a CSV file.

    Args:
        filename (str): The path to the CSV file.
        row_index (int): The 0-based index of the row to update.
        column_header (str): The header of the column to update.
        new_value (str): The new value to set.

    Returns:
        None
    """
    rows = []
    try:
        with open(filename, 'r', newline='') as infile:
            reader = csv.DictReader(infile)
            headers = reader.fieldnames
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return
    except IOError as e:
        print(f"IOError: {e}")
        return

    try:
        column_index = headers.index(column_header)
    except ValueError:
        print(f"Error: Column '{column_header}' not found in the CSV.")
        return

    if 0 <= row_index < len(rows):
        rows[row_index][column_header] = new_value
    else:
        print(f"Error: Row index {row_index} is out of bounds.")
        return

    with open(filename, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)