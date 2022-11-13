f = open("test.txt",'w')
print(f.name)
print(f.mode)
f.write("Python is awesome!")

print(f.closed)
f.close()

file = open('test.txt','a')
file.write('Not so good!')
file.close()

f = open('test.txt','r+')
print(f.read())
f.write("I love JavaScript")
f.close()
f = open('test.txt','r+')
print(f.read())
f.write('')
f.close()

