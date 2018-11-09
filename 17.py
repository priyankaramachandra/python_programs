# Implement a program using CLA for simple arithmetic calculator exmaple: operand operator operand ie. 10 + 10 / 30 * 20

import sys
a=sys.argv[1]
b=sys.argv[2]

sum=int(a)+int(b)
print("sum equal",sum)

sub=int(a)-int(b)
print("differnce = ",sub)

div=float(a)/float(b)
print("division = ",div)

mul=int(a)*int(b)
print("multiplication = ",mul)

div1=int(a)//int(b)
print("double division = ",div1)
