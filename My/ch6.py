lst = []
for i in range(1, 9, 1):
    lst.append(i)

print(lst)
print(id(lst))

lst1 = lst
print(lst1)
print(id(lst1))

lst2 = lst[::]
print("&(lst2)", id(lst2))

lst3 = lst
print("&(lst3)", id(lst3))
lst3 = [3,4,5]
print("&(lst)", id(lst3))

lst[:] = []

print("lst", lst)
print("lst1", lst1)
print("lst2", lst2)
print("lst3", lst3)
