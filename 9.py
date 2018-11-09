# Implement a program to create a dictionary of students with Registration number and names. Perform the two operations, insert and delete. 

details={"priya":1,"riya":2,"pooja":3}
print(details)

details["ritu"]=4
print(details)

details.pop("riya")
print(details)

details.popitem()
print(details)

del details["priya"]
print(details)