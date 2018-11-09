#Implement a program to check the total number of students. (create a sample file with RegNo, StudentName, Branch)

import csv
import sys
count=0
file=open("details.csv",'r')
line=csv.reader(file)
for row in line:
	count=count+1
	print(row)
print("total count of students present",count)