#Implement a program to write a line from the console to a file.

import sys
for i in range(1,len(sys.argv)):
	a=sys.argv[i]
	file=open("write.txt","a")
	file.write(a)
	