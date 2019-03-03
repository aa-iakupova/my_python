text='Мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог'
lst=list(text.split(' '))
print(lst)
new_lst=[]
for i in lst:
    if i[0].upper()=='М':
        continue
    new_lst.append(i)
result=' '.join(new_lst)
print(result)
