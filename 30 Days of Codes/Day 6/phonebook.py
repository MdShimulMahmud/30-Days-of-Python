contact_no = {"Sam": 1234,"Shimul": 1804021, "Yahan":1804007,"Bappi": 1804027}
x = 0

while x < 5:
    print("Enter your Name(pressed ENTER to exit): ")
    name = input()

    if name =='':
        break
    
    if name in contact_no:
        print("The contact number is "+ str(contact_no[name]))
    else:
        decision = input("There is no such number in your contact. Do you want to add it?: ")

        if decision == 'yes':
            number = input('Enter the new number: ')
            contact_no[name] = number
        else:
            quit = input("Do you want to quit?")
            if quit == 'yes':
                break
            else:
                print('Keep searching! ')

    x = x + 1
