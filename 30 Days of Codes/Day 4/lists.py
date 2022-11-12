# list = [1,2,3,4,5,6]
# print(list)

# list.append(9)
# print(list)

a = ['a','b',[1,2,5,[6,7,8]]]

# print(a[2][3][2])

# print(type(a))

# a.remove('b')
# print(a)

# print(a[-1][-1][-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[-3:-1])

# second_list = [1,2,3,4,5,3]

# thislist.append(second_list)
# print(thislist)
# thislist.extend(second_list)
# print(thislist)

# thislist.remove(2)
# print(thislist)

# thislist.pop(3)
# print(thislist)

# del thislist[3]
# print(thislist)

# thislist.clear()
# print(thislist)
# print(thislist, sep=",")
# s ="_".join(thislist)

# print(thislist)
# for i in thislist:
#     print(i,  end=" ")

# thislist.sort(reverse = True)
# print(thislist)


# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


# x = thislist.copy()
x = list(thislist)
print(x)