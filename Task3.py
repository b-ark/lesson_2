# немного усложнил задачу, сделал так, 
# чтобы необходимые числа можно было ввести через консоль

num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')

num1 = int (num1)
num2 = int (num2)

print('Сумма = ', num1 + num2 )
print('Разница = ', num1 - num2)
print('Частное = ', num1 / num2)
print('Произведение = ', num1 * num2)
print('Экспонента = ', num1 ** num2)
print('Модуль 1 числа = ', abs(num1))
print('Модуль 2 числа = ', abs(num2))
print('Целочисленное деление = ', num1 // num2)
# добавил остаток от деления, просто потому что могу :)
print('Остаток от деления = ', num1 % num2)