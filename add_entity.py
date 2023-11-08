import csv

# Define the CSV file path
csv_file = 'pipeline/lookup.csv'

# Define the specified starting number
starting_number = 65000000  # Change this to your desired starting number

data = []
with open(csv_file, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Update the 'entity' field with the specified starting number
for i, row in enumerate(data):
    row['entity'] = starting_number + i


with open(csv_file, mode='w', newline='') as file:
    fieldnames = ['prefix', 'resource', 'organisation', 'reference', 'entity']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for row in data:
        writer.writerow(row)

print(f"Entity numbers starting from {starting_number} have been added to the CSV file.")
