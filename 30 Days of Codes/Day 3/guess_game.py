import random as rn

secret_age = rn.randint(1,10)
check = True

def guess_game(guessed_age,secret):
    if guessed_age > secret:
       return print("Too high!")
    elif guessed_age < secret:
        return print("Too low!")
    else:
       return "Correct!"

for i in range(5):
        print("Take a guess! You have "+str(5-i)+" guesses left.")
        guess = int(input())
        if guess_game(guess,secret_age) == "Correct!":
            check = False
            break
    

if check:
    print("You lost! The secret age was "+str(secret_age))
else:
    print("Yon won the game!")