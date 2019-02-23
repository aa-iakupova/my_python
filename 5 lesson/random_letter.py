#Задан список слов: [‘самовар’, ‘весна’, ‘лето’]
#Выбираем случайное слово: ‘весна’
#Выбираем случайную букву: ‘с’
#Выводим на экран: ве?на
#Пользователь пытается угадать букву.

l=['самовар', 'весна', 'лето']
import random
x=random.randint(0,2)
print ('x',x)
word=l.pop(x)
print ('w',word)
y=random.randint(0,len(word)-1)
print ('y',y)
letter=word[y]
print('l',letter)
print(word[0:y]+'?'+word[y+1:])
guess=str(input('Введите букву '))
if guess==word[y]:
    print ('Победа!\nСлово:',word)
else:
    print('Увы! Попробуйте в другой раз')

