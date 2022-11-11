
"""
while True:
    print("Enter your name:")
    name = input()
    if name != "shimul":
        break
    else:
        print("Wrong name")

print("Thank you "+ name)
"""
"""
while True:
    print("Enter your age:")
    age = input()
    if age == "shimul":
        continue
    if int(age) < 1:
        print("Please enter a positive number")
        continue
    break
"""

# seriec of number
# sum = 0
# for c in range(1,10,2):
#     sum= sum + c**2
# print(sum)

# series = 1+(1+2)+(1+2+3)+(1+2+3+4)
sum  = 0
for i in range(1,5):
    for j in range(1,i+1):
        sum+=j
print(sum)
