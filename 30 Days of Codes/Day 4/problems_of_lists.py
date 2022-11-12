fav_movie = []

while True:
    print("Movie no " + str(len(fav_movie)+1) + " or press enter to exit!")
    movie = input()

    if movie =='':
        break
    fav_movie = fav_movie + [movie]

if len(fav_movie)!=0:
    print("Movie lists are : ")
    for i in range(len(fav_movie)):
        print(fav_movie[i])
print(" ")

guessed_movie = input("Enter a guessed movie name: ")

if guessed_movie not in fav_movie:
    print("Movie name doesn't exit in the lists!")
else:
    print("Your movie are in here!")