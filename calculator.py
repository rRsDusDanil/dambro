itog = 'Итог: %s'
print('Калкулятор.')
print('Выберите а и б:')
a = int(input('a ')) # Выбор переменной А
b = int(input('b ')) # Выбор переменной B
print('Выберите действие:')
print('1 +')
print('2 -')
print('3 *')
print('4 :')
c = int(input('Действие:')) # Выбор действия
if c == 1:
    d = a + b
if c == 2:
    d = a - b     # Действия
if c == 3:
    d = a * b
if c == 4:
    d = a / b
print(itog % d)
zyx = input('Чтобы выйти, нажмите ENTER.')  # Итог с значением результата в конце2