import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"


def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Ошибка: невозможно извлечь корень из отрицательного числа"


def calculator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Нахождение корня")
        print("0. Выход")

        choice = input("Введите номер операции (1/2/3/4/5/0): ")

        if choice == '0':
            print("Выход из калькулятора.")
            break

        if choice not in ('1', '2', '3', '4', '5'):
            print("Ошибка: некорректный ввод операции.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            if choice != '5':
                num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите числа для выполнения операции.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print("√", num1, "=", square_root(num1))


calculator()
