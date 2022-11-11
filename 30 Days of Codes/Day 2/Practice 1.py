#problem 1

x = int(input())
if x%400==0 :
    print("leap year")
elif x%100==0:
    print("Not a Leap year")
elif x%4==0:
    print("leap year")
else:
    print("Not leap year")


#problem 2
 
x = int(input("No of rows: "))

for i in range(0,x):
    for j in range(0,x-i-1):
        print(end=" ")

    for k in range(0,i+1):
        print("*",end="")
    print(" ")
