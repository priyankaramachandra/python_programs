#Implement a function to count the number of vowels present in the file. 


def vowel_count(string):

	count = 0
	vowels = ['a', 'e', 'i', 'o', 'u']
	for i in string:
		if i in vowels:
			count += 1

	return count



def main():

	file  = open("file1.txt")
	text = file.read()
	file.close()

	print("Vowel count in  file1.txt: ", vowel_count(text))



if __name__=="__main__":
	main()