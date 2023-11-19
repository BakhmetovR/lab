def add_user(user_list):
    user = {}
    user['Name'] = input("Введите имя: ")
    user['Surname'] = input("Введите фамилию: ")

    while True:
        try:
            user['Age'] = int(input("Введите возраст: "))
            break
        except ValueError:
            print("Ошибка: Возраст должен быть числом.")

    user['Address'] = input("Введите адрес: ")
    user['Username'] = input("Введите имя пользователя: ")

    while True:
        email = input("Введите почту: ")
        if not any(u['Username'] == email for u in user_list):
            user['Email'] = email
            break
        else:
            print("Ошибка: Почта уже занята.")

    # Валидация пароля
    while True:
        password = input("Введите пароль (минимум 8 символов): ")
        if len(password) >= 8:
            user['Password'] = password
            break
        else:
            print("Ошибка: Пароль должен содержать минимум 8 символов.")

    user_list.append(user)
    print("Пользователь добавлен успешно.")


def view_users(user_list):
    if not user_list:
        print("Список пользователей пуст.")
    else:
        for i, user in enumerate(user_list, 1):
            print(f"{i}. {user['Name']} {user['Surname']} ({user['Username']})")


def delete_user(user_list):
    view_users(user_list)
    if not user_list:
        print("Список пользователей пуст.")
        return

    while True:
        try:
            choice = int(input("Выберите пользователя для удаления (введите номер): "))
            if 1 <= choice <= len(user_list):
                del user_list[choice - 1]
                print("Пользователь удален успешно.")
                break
            else:
                print("Ошибка: Некорректный выбор пользователя.")
        except ValueError:
            print("Ошибка: Введите число.")


def login(user_list):
    email = input("Введите почту: ")
    password = input("Введите пароль: ")

    for user in user_list:
        if user.get('Email') == email and user.get('Password') == password:
            print("Вход выполнен успешно.")
            return

    print("Ошибка: Неверная почта или пароль.")


def main():
    user_list = []

    while True:
        print("\nВыберите действие:")
        print("1. Добавить пользователя")
        print("2. Посмотреть список пользователей")
        print("3. Удалить пользователя")
        print("4. Войти в систему")
        print("5. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':
            add_user(user_list)
        elif choice == '2':
            view_users(user_list)
        elif choice == '3':
            delete_user(user_list)
        elif choice == '4':
            login(user_list)
        elif choice == '5':
            print("Программа завершена.")
            break
        else:
            print("Ошибка: Некорректный выбор действия.")


if __name__ == "__main__":
    main()
