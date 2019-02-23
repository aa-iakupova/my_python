
film=str(input("Выбрать фильм: "))
day=str(input("Выбрать день(сегодня или завтра): "))
time=str(input("Выбрать время: "))
num=int(input("Выбрать количество билетов: "))

print("Выбрали:", film,'День:',day, 'Время:',time,'Количество билетов:', num)

def price(num):
    if film=='Пятница':
        if time=='12':
            return 250*num
        if time=='16':
            return 350*num
        if time=='20':
            return 450*num
    if film=='Чемпионы':
        if time=='10':
            return 250*num
        if time=='13':
            return 350*num
        if time=='16':
            return 350*num
    if film=='Пернатая банда':
        if time=='10':
            return 350*num
        if time=='14':
            return 450*num
        if time=='18':
            return 450*num
    else:
        return "Ошибка ввода"

if price(num)=='Ошибка ввода':
    print (price(num))
else:
    if day=='завтра':
        if num>=20:
            price_with_discount=int(price(num)*0.75)
            print('Итого со скидкой:',price_with_discount,'руб')
        else:
            price_with_discount=int(price(num)*0.95)
            print('Итого со скидкой:',price_with_discount,'руб')
    else:
        if num>20:
            price_with_discount=int(price(num)*0.80)
            print('Итого со скидкой:',price_with_discount,'руб')


