s = '''В разные эпохи и у разных народов число Пи имело разное значение. Например, в Древнем Египте оно равнялось 3.1604 у индусов оно приобрело значение 3.162 китайцы пользовались числом, равным 3.1459 Буквенное обозначение число Пи получило только в 1706 году – оно происходит от начальных букв двух греческих слов, означающих окружность и периметр. Буквой π число наделил математик Джонс, а прочно вошла в математику она уже в 1737 году.'''
#not quite sure

lst=s.split(' ')
new_lst=[]

for i in lst:
    try:
        new_lst.append(float(i))
    except ValueError:
        continue

print(new_lst)
print('Количество цифр: ',len(new_lst))
summ=0
for i in new_lst:
    summ+=i
print('Сумма: ',summ)
print('Максимальное: ',max(new_lst))

