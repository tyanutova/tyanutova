def checkpassword():
    a = input("Введите пароль: ")
    b = input("Подтвердите пароль: ")

    if a == b:
        print("Пароль принят")
    else:
        print("Пароль не принят")
checkpassword()