import random
import smtplib, ssl
def load_passwords_and_logs(file, names, passwords):
    with open(file, 'r') as f:
        data = f.readlines()
        for line in data:
            parts = line.strip().split(',')
            names.append(parts[0])
            passwords.append(parts[1])
def generate_password():
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    return psword
def check_password_requirements(password):
    has_digit = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in "!@#$%^&*()" for char in password)
    return has_digit and has_lower and has_upper and has_special
def register_user(names, passwords, emails, new_username, new_password, new_email):
    names.append(new_username)
    passwords.append(new_password)
    emails.append(new_email)
    print("User registered successfully.")
def authorize_user(names, passwords, entered_username, entered_password, entered_email, emails):
    if entered_username in names:
        index = names.index(entered_username)
        if passwords[index] == entered_password and emails[index] == entered_email:
            print("Authorization successful.")
        else:
            print("Authorization failed. Incorrect password or email.")
    else:
        print("User not found. Please register.")
def change_user_credentials(operation, names, passwords, emails, current_username, new_username, new_password, new_email):
    if operation == "username":
        if current_username in names:
            index = names.index(current_username)
            names[index] = new_username
            print("Username changed successfully.")
        else:
            print("User not found. Please register.")
    elif operation == "password":
        if current_username in names:
            index = names.index(current_username)
            passwords[index] = new_password
            print("Password changed successfully.")
        else:
            print("User not found. Please register.")
    elif operation == "email":
        if current_username in names:
            index = names.index(current_username)
            emails[index] = new_email
            print("Email changed successfully.")
        else:
            print("User not found. Please register.")
    else:
        print("Invalid operation. Please choose 'username', 'password', or 'email'.")
def recover_password(names, passwords, emails, entered_username):
    if entered_username in names:
        index = names.index(entered_username)
        print(f"Your password is: {passwords[index]}. Please remember it.")
    else:
        print("User not found. Please register.")
    
def send_password_email(to_email, parool):
    from email.message import EmailMessage
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "david.nikolajev07@gmail.com"
    password = "sjik wdnu jsmh ettg"      
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(f"Your password is {parool}")
    msg['Subject'] = "Your password!"
    msg['From'] = sender_email
    msg['To'] = to_email
    
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.send_message(msg)

    except Exception as e:
        print(e)
    finally:
        server.quit()
