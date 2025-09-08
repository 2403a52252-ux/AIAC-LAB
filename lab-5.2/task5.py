def greet_user():
    name = input("Enter your name: ")
    gender = input("Enter your gender (male/female/other): ").lower()
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    else:
        title = "Mx."
    print(f"Hello, {title} {name}!")

greet_user()