#Implement a program to convert the input string to upper case (without using standard library)
str=input("string in lower case\n")
new_str=''
for char in str:
    new_str+= chr(ord(char) - 32)
print("string in uppercase:",new_str)
