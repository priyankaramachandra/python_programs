#Implement a program to check the elements of a list is a palindrome or not.

def is_palindrome(my_list): 
	list_copy = my_list.copy()
	list_copy.reverse()
	if my_list == list_copy:
		return True
	return False


def main():
	

	list1= [ 1, 3 , 3, 1 ]

	list1_copy = list1.copy()

	list2= [1, 3 ,'h', 4, 1 ]

	print("list1:", list1)
	print("list2:", list2)

	if(is_palindrome(list1)):
		print("list1 is palindrome")
	else:
		print("list1 is not a is not apalindrome")

	if(is_palindrome(list2)):
		print("list2 is not a palindrome")
	else:
		print("list2 is not a apalindrome")

if __name__=="__main__":
	main()