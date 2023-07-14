import json
import csv

with open('input.json') as file:
    data = json.load(file)

filename = 'output.csv'

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Key','Value1', 'Value2'])

    for item in data:
        for key, value in item.items():
            if isinstance(value, list):
                value1, value2 = value
                writer.writerow([key, value1, value2])
            else:
                writer.writerow([key, value, ''])
                 


print(f"Data written to {filename} successfully!")
