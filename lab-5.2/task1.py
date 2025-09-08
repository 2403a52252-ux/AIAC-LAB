import hashlib
import getpass
# Simple in-memory user database (username: hashed_password)
users_db = {}
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def register():
    username = input("Enter new username: ")
    if username in users_db:
        print("Username already exists.")
        return
    password = getpass.getpass("Enter new password: ")
    users_db[username] = hash_password(password)
    print("Registration successful.")
def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    hashed = hash_password(password)
    if users_db.get(username) == hashed:
        print("Login successful.")
    else:
        print("Invalid username or password.")
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()