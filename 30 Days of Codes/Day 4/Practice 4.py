# linear search
"""
num = []
n = int(input())
for i in range(n):
    x = int(input())
    num+=[x]
check_num = int(input())
print(num)

if check_num in num:
    print("Yes")
else:
    print("No")
"""
# binary search
"""

num = []
n = int(input())

for i in range(n):
    x = int(input())
    num+=[x]

s = int(input("Enter your number : "))
num.sort()
print(num)
low, high = 0, len(num)-1
check = False

while low<=high:
    mid = int((low + high)/2)
    if num[mid]==s:
        check = True
        break
    elif s > num[mid]:
        high = mid - 1
    else:
        low = mid + 1

if not check:
    print("Not found")
else:
    print("Found")
"""

# odd lists

lists = [1,2,3,3,4,5,6,7,8,9]

def odd_numbers(one_list):
    new_list = []
    for i in range(len(one_list)):
        if one_list[i]%2 != 0:
            new_list.append(one_list[i])
    return new_list

print(odd_numbers(lists))