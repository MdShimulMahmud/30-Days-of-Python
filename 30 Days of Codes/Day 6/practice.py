# digit counts

def digit_counter(n):
    if n == 0:
        return 0
    return 1 + digit_counter(n//10)

print(digit_counter(1234))

# exponent
def exponent(n,m):
    if m == 0:
        return 1
    elif m % 2 == 0:
        return exponent(n,m//2) * exponent(n,m//2)
    else:
        return n * exponent(n,m//2) * exponent(n,m//2)


print(exponent(2,3))