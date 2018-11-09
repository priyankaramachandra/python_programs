#Implement a  program to check the count of vowels in a given string.(with repeated occurance)

string=input("enter a string")
def count(string):
	vowels = ['a', 'e', 'i', 'o', 'u']

	count = 0

	for i in string:
		if i in vowels:
			count = count+1

	print("the total count is",count)
count(string)