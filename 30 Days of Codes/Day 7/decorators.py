# def outer(message):
#     print("I am from outer function!")

#     def inner():
#         print("I am from inner function! ")
#         print(f"Passing message : {message}")
#     return inner 

# x = outer("Hello Shimul")
# x()

def decorator(original_func):
    print(f"wrapper executed before {original_func.__name__}() ")

    def wrapper():
        if 10 > 5:
            print("Yes, it is true!")
        
        return original_func() + "extra string"

    return wrapper