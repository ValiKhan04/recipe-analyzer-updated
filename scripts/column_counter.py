import csv
import os

def print_column(column_index, path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        #next(reader)  # Skip header row if present

        column_Name = next(reader)
        counter_of_nonBlank = 0
        for row in reader:
            if len(row) > column_index:
                if (row[column_index]== ""):
                    continue
                else:
                    counter_of_nonBlank += 1
        print(column_Name[column_index]+": "+ str(counter_of_nonBlank))

# Example usage
csv_directory = "/output"
csv_file = 'merged_deleted_duplicates.csv'




column_index = 0
print(csv_file + " contents")

parent_directory = os.path.dirname(os.getcwd())  # Get the parent directory path

file_path = os.path.join(parent_directory + csv_directory, csv_file)  # Construct the file path

with open(file_path, 'r') as file:
        reader = csv.reader(file)
        column_Name = next(reader)

        while (column_index < len(column_Name)):
            print_column(column_index, file_path)
            column_index+=1
# SAMPLE DATA OUTPUT #
# branded_food.csv contents #
# fdc_id: 1845297 #
# brand_owner: 1830879 #
# brand_name: 1297928 #
# subbrand_name: 87051 #
# gtin_upc: 1845297 #
# ingredients: 1839909 #
# not_a_significant_source_of: 73496 #
# serving_size: 1834517 #
# serving_size_unit: 1826269 #
# household_serving_fulltext: 765642 #
# branded_food_category: 1834725 #
# data_source: 1845297 #
# package_weight: 706033 #
# modified_date: 1845277 #
# available_date: 1845297 #
# discontinued_date: 0 #
# market_country: 1845297 #
# trade_channel: 15579 #
# preparation_state_code: 39151
# short_description: 39267 #