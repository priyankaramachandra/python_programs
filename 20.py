#Implement a program to find the euclidean distance of two points. 

x1=int(input("enter x1"))
y1=int(input("enter y1"))
x2=int(input("enter x2"))
y2=int(input("enter y2"))

eq=(x2-x1)**2
eq1=(y2-y1)**2
result=(eq+eq1)**0.5
print("the euclidean distance is",result)
