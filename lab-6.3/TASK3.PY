age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age")
else:
    if age < 13:
        print("Child")
    else:
        if age < 20:
            print("Teenager")
        else:
            if age < 60:
                print("Adult")
            else:
                print("Senior")