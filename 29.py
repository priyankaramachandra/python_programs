# In a given list find the total number of odd numbers, even numbers and their respetive sum and average.

list1=[1,2,3,4,5,6]
a=0
b=0
count=0
count1=0
avg=0
avg1=0
for i in list1:
	if(i%2==0):
		a=a+i
		count=count+1
		
	else:
		b=b+i
		count1=count1+1

avg=a/count
avg1=b/count1
	
print(list1)
print("total of even numbers",a)
print("total of odd numbers",b)
print("total count of even numbers",count)
print("total count of odd numbers ",count1)
print("average of even numbers",avg)
print("average of odd numbers",avg1)
