#1
new_list=[]
for i in [2,4,9,16,25]:
    new_list.append(i**2)
print(new_list)

#2
print(list(map(lambda x: x**2,[2,4,9,16,25])))

#3
print([x**2 for x in [2,4,9,16,25]])
