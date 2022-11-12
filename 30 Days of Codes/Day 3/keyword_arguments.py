# name = input("Enter your name: ")
# student_id = input("Enter your student ID: ")
# print("Your name is {} and your student ID is {}".format(name, student_id))
# print(name)

#Exception handling

def func(x):
    try:
        return int(100/x)
    except:
        print("There is an division by zero error")


print(func(10))