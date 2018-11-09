# Implement a program with lamda functions, for finding the area of circle, triangle, square.

def circle(r):
    return lambda a:a*r*r
    
circle1=circle(3)
print("area of circle",circle1(3.14))

def triangle(b,h):
    return lambda r:r*b*h
    
triangle1=triangle(3,4)
print("area of triangle ",triangle1(0.5))

def square(l):
    return lambda a:a+l*l

square1=square(3)
print("area of square",square1(0)) #zero is constant as area of square formula is l*l