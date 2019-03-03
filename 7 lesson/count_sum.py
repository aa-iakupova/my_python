number=str(input('Введите число '))
total=0
for i in number:
    if int(i)%2==0:
        continue
    total+=int(i)**2

print(total)
