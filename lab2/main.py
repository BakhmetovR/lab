# 1

x = int(input('Введите первое число '))
y = int(input('Введите первое число '))
z = (x**2 + y**2)**0.5
print(z)

# 2

lesson_number = int(input('Введите номер урока: '))
total_minutes = lesson_number * 45 + (lesson_number // 2) * 5 + ((lesson_number - 1) // 2) * 15
hours = total_minutes // 60
minutes = total_minutes % 60
print(9 + hours, minutes)

# 3

x = int(input('Введите первое число '))
y = int(input('Введите второе число '))
if x > y:
    print(1)
elif y > x:
    print(2)
else:
    print(0)

# 4

x = int(input('Введите первое число '))
y = int(input('Введите второе число '))
z = int(input('Введите третье число '))
if x >= y and x >= z:
    q = x
elif y >= x and y >= z:
    q = y
else:
    q = z
print(q)

# 5



if x == y == z:
    print(3)
elif x == y or x == z or y == z:
    print(2)
else:
    print(0)

# 6

x = int(input('Введите первое число '))
y = int(input('Введите второе число '))
z = int(input('Введите третье число '))

if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x

print(x, y, z)
