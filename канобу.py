import random
import time

print('КАМЕНЬ-НОЖНИЦЫ-БУМАГА')

print('---------------------')
print('----НАЧАТЬ(ENTER)----')
print('---------------------')

q = input()

print('---------------------')
print('------КАМЕНЬ(1)------')
print('-----НОЖНИЦЫ(2)------')
print('------БУМАГА(3)------')
print('---------------------')

vib = int(input('ВЫБОР: '))
print('Подождите, бот выбирает...')
time.sleep(3)
bot = random.randint(1,3)
if bot == 1 and vib == 3:
    print('У бота был камень. Вы победили!')
if bot == 1 and vib == 2:
    print('У бота был камень. Вы проиграли!')
if bot == 1 and vib == 1:
    print('У бота был камень. Ничья!')
if bot == 2 and vib == 3:
    print('У бота были ножницы. Вы проиграли!')
if bot == 2 and vib == 2:
    print('У бота были ножницы. Ничья!')
if bot == 2 and vib == 1:
    print('У бота были ножницы. Вы выиграли!')
if bot == 3 and vib == 3:
    print('У бота была бумага. Ничья!')
if bot == 3 and vib == 2:
    print('У бота была бумага. Вы выиграли!')
if bot == 3 and vib == 1:
    print('У бота была бумага. Вы проиграли!')
o = input('Нажмите ENTER, чтобы выйти.')