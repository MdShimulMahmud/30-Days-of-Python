
file = open("practice.txt",'w')

file.write("123321")
file.close()

f = open('practice.txt','r+')
text = list(f.read())
f.close()
print(text)
flag = True
for i in range(len(text)):
    if text[i] != text[len(text)-i-1]:
        flag = False
        f = open('practice.txt','w')
        for i in range(len(text)):
            f.write("0")
        f.close()
        break
   
if flag:
    print("Yes")
else:
    print("No")

