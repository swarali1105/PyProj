import csv

# create data to write to CSV file
data = [
    ['Name', 'Age', 'Country'],
    ['John', '30', 'USA'],
    ['Jane', '25', 'Canada'],
    ['Bob', '40', 'Australia'],
]

# open a file for writing and create a CSV writer object
with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # write the data to the CSV file
    for row in data:
        writer.writerow(row)

print('CSV file created successfully.')
