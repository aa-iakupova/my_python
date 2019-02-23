# на основе prog2.py
value = input("Введите атомный номер элемента: ")
if value:
    n = int(value)
    if n == 3:
        print("Это Li, литий")
    elif n==25:
        print("Это Mn, марганец")
    elif n==80:
        print("Это Hg, ртуть")
    elif n==17:
        print("Это Cl, хлор")
    else:
        print("Что это?!")
else:
    print("Введите целое число!")

#Li, Mn, Hg, Cl
