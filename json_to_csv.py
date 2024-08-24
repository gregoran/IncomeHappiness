import json
import csv

# Path to the input JSON file
json_file_path = r'C:\Users\DELL\Desktop\Customer Segmentation and Behaviour\DC Purchase Orders - 2017.json'

# Path to the output CSV file
csv_file_path = r'C:\Users\DELL\Desktop\Customer Segmentation and Behaviour\DC_Purchase_Orders_2017.csv'

# Open the JSON file and load the data
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Extract the data you want to write to CSV
# Assuming that data is a list of dictionaries
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header (keys of the dictionary)
    header = data[0].keys()
    csv_writer.writerow(header)

    # Write the data (values of the dictionary)
    for entry in data:
        csv_writer.writerow(entry.values())

print("JSON to CSV conversion completed successfully!")
