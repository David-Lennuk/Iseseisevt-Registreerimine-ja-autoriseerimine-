﻿from MyModule import *


while True:
    print("\n1-Регистрация\n2-Авторизация\n3-Изменение пароля\n4-Восстановление забытого пароля\n5-Прекращение")

    choice=input("Выберите действие: ")

    if choice=="1":
        username=input("Введите логин: ")
        password=input("Введите пароль: ")
        print(username, password)

    elif choice=="2":
        username=input("Введите логин: ")
        password=input("Введите пароль: ")
        print(username, password)

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
