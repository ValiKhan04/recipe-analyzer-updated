import csv
import os

def removeDuplicates(column_index, path):

    with open(path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)  

    unique_rows = [] 
    hashset = set() 

    for row in rows:
        value = row[column_index]
        if value not in hashset:
            hashset.add(value)
            unique_rows.append(row)

    csv_directory = "/output"
    # Create a new file for writing the rows with unique values
    output_file = 'merged_deleted_duplicates.csv'

    parent_directory = os.path.dirname(os.getcwd())

    file_path = os.path.join(parent_directory + csv_directory, output_file)

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(unique_rows) 

    print("File Path: " + path)
    print("Column Name: " + header[column_index])
    print("Total Rows: " + str(len(rows)))
    print("Unique Rows: " + str(len(unique_rows)))
    print("Duplicate Rows: " + str(len(rows) - len(unique_rows)))

# Example usage
csv_directory = "/output"
csv_file = 'merged.csv'

parent_directory = os.path.dirname(os.getcwd())  # Get the parent directory path

file_path = os.path.join(parent_directory + csv_directory, csv_file)

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    column_Name = next(reader)
    removeDuplicates(0, file_path)
