
password_bank = {"Sam": 1234,"Shimul": 1804021, "Yahan":1804007,"Bappi": 1804027}

matched = False
x = 0


while x < 5:
    print("Enter your name: ")
    name = input()
    if name in password_bank:
        for i in range(0,3):
            password = int(input("Enter your password: "))
            if password in password_bank.values():
                matched = True
                print("Access granted!")
                break
            else:
                print("Wrong password. Try again!"+" "+" You have left "+str(2-i)+" more tries.")
    else:
        print("Name doesn't exists!")
    x = x + 1

    if matched:
        break

