
import random
comp=random.randint(1,101)
print('Компьютер загадал число от 1 до 100.\nУ вас есть три попытки. Удачи!\n')

n=3
while n!=0:
    guess=int(input('Попробуйте угадать: '))
    if comp==guess:
        break
    elif guess>comp:
        print('Попробуйте число меньше!')
        n-=1
    else:
        print('Попробуйте число больше!')
        n-=1
print('Число: ',comp)
