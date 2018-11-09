# Implement a progam to convert the input string to inverse case(upper->lower, lower->upper) ( without using standard library)

str=input("enter a string\n")
res=''
res1=''
for char in str:
	if ord(char)>=97 and ord(char)<=122:
		result=ord(char) - 32
		res1=chr(result)
		res=res+res1
	else:
		result=ord(char) + 32
		res1=chr(result)
		res=res+res1

print(res)