summ=0
print ('Введите три числа и я посчитаю их сумму!')
n=3
while n!=0:
    number=input('Введите число или Стоп для выхода: ')
    if number.upper()=='СТОП':
        break
    elif number.isdigit:
        summ+=int(number)
        n-=1
    else:
        print('Ошибка ввода')

print('Сумма: ',summ)
