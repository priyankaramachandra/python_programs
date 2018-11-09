# Find the average number of students from records

import csv
import sys
count=0
total=10
file=open("details.csv",'r')
line=csv.reader(file)
for row in line:
	count=count+1
	print(row)
print("total count of students present",count)
average=float(count)/float(total)
print("average of students present in record ",average )
