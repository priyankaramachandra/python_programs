#Implement a progam to convert the input string to lower case ( without using standard library)

str=input("string in uppercase letter\n")
new_string=''
for char in str:
    #print(ch)
    new_string+= chr(ord(char) + 32)
print("string in lowercase:",new_string)