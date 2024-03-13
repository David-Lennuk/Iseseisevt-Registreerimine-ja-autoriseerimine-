from MyModule import *
registered_users = {"Anton": "Mark5527", "Erik": "Tanki2"}

while True:
    print("\n1-Регистрация\n2-Авторизация\n3-Изменение пароля\n4-Восстановление забытого пароля\n5-Прекращение")

    choice=input("Выберите действие: ")

  if choice == "1":
        username = input("Введите имя пользователя: ")
        if username in registered_users:
            print("Имя пользователя уже занято. Пожалуйста, выберите другое имя пользователя.")
            continue
        password_choice = input("Хотите ли вы создать пароль автоматически (авто) или вручную (вручную): ")
        if password_choice == "авто":
            password = MyModule.generate_password_auto()
        elif password_choice == "вручную":
            password = MyModule.generate_password_manual()
        registered_users[username] = password
        print("Пользователь успешно зарегистрирован.")

    elif choice=="2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in registered_users and registered_users[username] == password:
            print("Авторизация прошла успешно.")
        else:
            print("Неверное имя пользователя или пароль.")

    elif choice=="3":
        username=input("Введите логин: ")
        old_password=input("Введите старый пароль: ")
        new_password=input("Введите новый пароль: ")
        print(username, old_password, new_password)

    elif choice=="4":
        username=input("Введите логин: ")
        print(username)

    elif choice=="5":
        print("Программа завершена.")
        break

    else:
        print("Неправильный ввод.")
