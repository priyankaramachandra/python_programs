# Implement a program for above using getopt.

import getopt
import sys
 

def usage():
    print("Addition: python 18.py -a <number1> -b <number2>")
    print("Subtraction: python 18.py -a <number1> -b <number2> --subtract") 
    print("Subtraction: python 18.py -a <number1> -b <number2> --multiply")
    print("Subtraction: python 18.py -a <number1> -b <number2> --divide")
    print('Example: python 18.py -a 10 -b 3\n')

def add(a, b):
    return a + b
 

def subtract(a, b):
    return a - b

def multiplication(a,b):
	return a*b    

def division(a,b):
	return a/b    

 
 
def main():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'ha:b:s:m:d', ['help','num1=', 'num2=', 'subtract','multiply','divide'])

    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
 
    num1 = num2 = None
    sub = False
    mul=False
    div=False
    
    
    if len(opts) != 0:
        
        for (o, a) in opts:
            if o in ('-h', '--help'):
                usage()
                sys.exit()
            elif o in ('-a', '--num1'):
                num1 = int(a)
            elif o in ('-b', '--num2'):
                num2 = int(a)
            elif o in '--subtract':
                sub = True
            elif o in '--muliply':
            	mul = True    
            elif o in '--divide':
            	div = True   	
            else:
                
                usage()
                sys.exit(2)
    else:
        
        usage()
        sys.exit(2)
 
    
    if num1 and num2:
        if sub:
            print ('\n Difference in two numbers is :', subtract(num1, num2), '\n')
        elif mul:
        	print("product of two numbers is:",multiplication(num1,num2))
        elif div:
        	print("division of two numbers is:",division(num1,num2))	 

        else:
            print ('\n Sum of two numbers is :', add(num1, num2), '\n')
    else:
        usage()
        sys.exit(2)
 
 
if __name__ == '__main__':
    main()