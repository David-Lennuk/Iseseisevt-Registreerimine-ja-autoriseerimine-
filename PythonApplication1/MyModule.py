def register(username, password, user_data):
    """Регистрирует нового пользователя.

    """
    if username in user_data:
        print("Пользователь с таким логином уже существует")
    else:
        user_data[username]=password
        print("Пользователь успешно зарегистрирован")

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