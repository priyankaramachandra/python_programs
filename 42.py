#Read the regno and name in the file, create a dictinary of these data.

import csv


with open('stud_details.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    students = dict()

    for row in csv_reader:
        students[row['RegNo']] = row['name']

    
    print(students)


