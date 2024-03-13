import random
import string
def generate_password_auto():
    """позволяет пользивателю создать пароль автоматически
    
    """
    special_chars = ".,:;!_*-+()/#¤%&"
    digits = '0123456789'
    lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
    uppercase_letters = string.ascii_uppercase
    password_list = list(special_chars + digits + lowercase_letters + uppercase_letters)
    random.shuffle(password_list)
    password = ''.join([random.choice(password_list) for _ in range(12)])
    return password
def generate_password_manual():
    """позволяет пользивателю создать пароль в ручную

    """
    while True:
        password = input("Enter a password: ")
        if not any(char.isdigit() for char in password):
            print("Password must contain at least one digit.")
            continue
        if not any(char.islower() for char in password):
            print("Password must contain at least one lowercase letter.")
            continue
        if not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase letter.")
            continue
        if not any(char in string.punctuation for char in password):
            print("Password must contain at least one special character.")
            continue

def login(username, password, user_data):
    """Авторизует пользователя.

    """
    if username in user_data and user_data[username]==password:
        print ("Авторизация успешна")
    else:
        print ("Неправильный логин или пароль")

def change_password(username, old_password, new_password, user_data):
    """Изменяет пароль пользователя.
    
    """
    if username in user_data and user_data[username]==old_password:
        user_data[username]=new_password
        print ("Пароль успешно изменен")
    else:
        print ("Неправильный логин или пароль")

def reset_password(username, new_password, user_data):
    """Сбрасывает пароль пользователя.
    
    """
    if username in user_data:
        user_data[username]=new_password
        print ("Пароль успешно сброшен")
    else:
        print ("Пользователь не найден")
