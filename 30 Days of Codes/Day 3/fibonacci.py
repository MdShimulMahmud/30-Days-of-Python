def fibonacci(n):
    if n==0:
        print("0")
    else:
        x,y = 0,1
        print(x,y,end=" ")
        for i in range(2,n):
            z = x+y
            print(z,end=" ")
            x,y = y,z

fibonacci(8)