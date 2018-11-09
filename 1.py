 #Implement a menu based  program for Arithemetic Calculator

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b 
    
def mod(a,b):
    return a%b 
    
def div1(a,b):
    return a//b 
    
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 
print("5.modulus")
print("6.doublediv")
print("7.exit")

choice = input("Enter choice(1/2/3/4/5/6/7):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    a=add(num1,num2)
    print("sum is", a)
elif  choice=='2':
    b=sub(num1,num2)
    print("sub is",b)
elif choice=='3':
    c=mul(num1,num2)
    print("product is",c)
elif choice=='4':
    d=div(num1,num2)
    print("div is",d)
elif choice=='5':
    e=mod(num1,num2)
    print("mod is",e)
elif choice=='6':
    f=div1(num1,num2)
    print("doublediv is",f)                
else:
    print("invalid")