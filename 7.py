# Implement a program to reverse a string (without standard librar function)

def reverse_string(string):
	return string[::-1]

def main():
	print(reverse_string(input("Enter string")))


if __name__ == "__main__":
	main()