import csv
import os

def duplicateCount(column_index, path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        counter = 0
        hashset = set()
        for row in reader:
            value = row[column_index]
            if value not in hashset:
                hashset.add(value)
            counter += 1
            if counter % 50000 == 0:
                print("Progress: " + str(counter))
        print("File Path: " + path)
        print("Column Name: " + header[column_index])
        print("Total Values Counted: " + str(counter))
        print("Length of Non-repeated Array: " + str(len(hashset))) 
        repeats = counter - len(hashset) 
        print("Duplicates: " + str(repeats))

# Example usage
csv_directory = "/output"
csv_file = 'merged.csv'

parent_directory = os.path.dirname(os.getcwd())  # Get the parent directory path

file_path = os.path.join(parent_directory + csv_directory, csv_file)

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    column_Name = next(reader)
    duplicateCount(0, file_path)
