itog = 'Итог: %s'
import time
print('Конвертер величин.')
print('-----------------------')
print('-----КМ,М,СМ,ММ(1)-----')
print('-----------------------')

q = int(input('Выбор: '))

print('Перевести -x- в -y-: ')
print('---X---')
print('1: (KM)')
print('2: (M) ')
print('3: (CM)')
print('4: (MM)')

x = int(input('Выбор: '))

print('---Y---')
print('1: (KM)')
print('2: (M) ')
print('3: (CM)')
print('4: (MM)')

y = int(input('Выбор: '))

x1 = int(input('Выберите переменную Х: '))

print('Перевожу...')
time.sleep(1)

if x == 1 and y == 2:
    d = x1 * 1000
    print(itog % d + ' метр')
if x == 1 and y == 3:
    d = x1 * 100000
    print(itog % d + ' сантиметр')
if x == 1 and y == 4:
    d = x1 * 1000000
    print(itog % d + ' милиметр')
if x == 2 and y == 1:
    d = x1 / 1000
    print(itog % d + ' километр')
if x == 2 and y == 3:
    d = x1 * 100
    print(itog % d + ' сантиметр')
if x == 2 and y == 4:
    d = x1 * 1000
    print(itog % d + ' милиметр')
if x == 3 and y == 1:
    d = x1 / 1000000
    print(itog % d + ' километр')
if x == 3 and y == 2:
    d = x1 / 100
    print(itog % d + ' метр')
if x == 3 and y == 4:
    d = x1 / 10
    print(itog % d + ' милиметр')
if x == 4 and y == 1:
    d = x1 / 10000000
    print(itog % d + ' километр')
if x == 4 and y == 2:
    d = x1 / 1000
    print(itog % d + ' метр')
if x == 4 and y == 3:
    d = x1 / 10
    print(itog % d + ' сантиметр')
input()