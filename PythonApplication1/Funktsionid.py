import smtplib
import ssl
from email.message import EmailMessage
from MyMoodul import *
names = []
passwords = []
emails = []
load_passwords_and_logs("konto.txt", names, passwords, emails)
while True:
    print("\n0-Show accounts\n1-Registration\n2-Authorization\n3-Change credentials\n4-Recover password\n5-Quit")

    choice = input("Choose an action: ")
    if choice == "0":
        print(f"{names}\n{passwords}\n{emails}")
    if choice == "1":
        new_username = input("Enter new username: ")
        new_email = input("Enter email: ")
        print("Do you want a randomly generated password? (yes/no)")
        choice_password = input()
        
        if choice_password.lower() == "yes":
            new_password = generate_password()
            print(f"Generated password: {new_password}")
        else:
            new_password = input("Enter password: ")
            while not check_password_requirements(new_password):
                print("Password requirements not met. Please try again.")
                new_password = input("Enter password: ")
        register_user(names, passwords, emails, new_username, new_password, new_email)
        print("User registered successfully.")
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in names:
            index = names.index(username)
            if passwords[index] == password:
                print("Authorization successful.")
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")
    elif choice == "3":
        username = input("Enter username: ")
        if username in names:
            index = names.index(username)
            new_password = input("Enter new password: ")
            while not check_password_requirements(new_password):
                print("Password requirements not met. Please try again.")
                new_password = input("Enter new password: ")
            passwords[index] = new_password
            rewrite("konto.txt", names, passwords, emails)
            print("Password changed successfully.")
        else:
            print("Username not found.")
    elif choice == "4":
        email = input("Enter email: ")
        if email in emails:
            index = emails.index(email)
            new_password = generate_password()
            passwords[index] = new_password
            rewrite("konto.txt", names, passwords, emails)
            send_password_email(email, new_password)
            print(f"New password sent to {email}")
        else:
            print("Email not found.")
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please select a valid option.")
