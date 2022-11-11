import math

#problem 1
a = int(input())
b = int(input())
c = int(input())
x1 = ((-b) + (math.sqrt(b**2 - 4*a*c))) / (2*a)
x2 = ((-b) -( math.sqrt(b**2 - 4*a*c)))/ (2*a)
print(int(x1), int(x2))

#problem 2
c = input("Enter celcius: ")
answer = ((9/5)*float(c))+32
print(answer)