import math
x=int(input('Введите число знаков после запятой '))
num=math.pi
def fun(x):
    number=round(num,x)
    return f'{number}'
print (fun(x))


