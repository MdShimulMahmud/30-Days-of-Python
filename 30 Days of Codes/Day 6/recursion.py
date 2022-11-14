# factorial 

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

num = input()
print(fact(int(num)))

