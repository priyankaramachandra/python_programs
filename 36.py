"""Implement a python code to get username and password. Validate using regular experssions.
 Conditions: Username should not exceed 10 characters. 
It can't have symbols. Password should have one upper case, one lower case, one number , 
one symbol and length minimum of 6.
"""
import re


def valid_username(string):
	#matches 0-9, underscore(_), uppercase and lowercase chars in range 1-10
	result = re.search(r'^[0-9a-zA-Z_]{1,10}$', string)
	if(result): return True
	else: return False

def valid_password(string):
	if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()_+=])[\w\d!@#$%^&*()_+=]{6,}$", string):
	    return True
	else:
	    return False

def main():
	username = input("Enter usernname\t")
	password = input("Enter password\t")

	if not valid_username(username):
		print("\nInvalid username."+
				"\nUsername length should be between 1-10 ." +
				"\n Username can have only numbers, letters and '_'")
		return


	if not valid_password(password):
		print("\nInvalid password."+
				"\nPassword should have one upper case, one lower case, one number , one symbol and length minimum of 6.")
		return


	print("\nValid username and password\n")





if __name__=="__main__":
	main()