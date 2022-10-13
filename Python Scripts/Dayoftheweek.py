from curses.ascii import isdigit
tries = 3
counter = 0

num = input("Hello user please enter an number between 1 - 7: ")

while num.isdigit():
    if num == "1":
        print("Monday")
        break
    elif num == "2":
        print("Tuesday")
        break
    elif num == "3":
        print("Wednesday")
        break
    elif num == "4":
        print("Thursday")
        break
    elif num == "5":
        print("Friday")
        break
    elif num == "6":
        print("Saturday")
        break
    elif num == "7":
        print("Sunday")
        break
    else:
        counter += 1
        if counter == tries:
            print(counter)
            print("You have exceeded the number of tries")
            break
else:
    print("Invalid input") 