import random

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


for i, elem in enumerate(lst):
    print(i, elem)
    lst[i] *= 2

print("-------------")

print(lst[:3])
print("-------------")

print(lst[0], lst[1], lst[2])
print("-------------")

for i in range(len(lst)):
    print(i, lst[i])
    lst[1] *= 2

print("ID - списка:", id(lst))
print("Список:", lst)
print("-------------")

lst1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
for i in range (len(lst1)):
    lst[i]**=2

print("ID - списка:", id(lst1))
print("Список в квадрате:", lst)
print("-------------")

lst = [0] * 100
print(lst)

def fill_list(lst, lower_bound, upper_bound):
    for i in range(len(lst)):
        lst[i] = random.randint(lower_bound, upper_bound)

fill_list(lst, 10, 20)
print("Рандомный список:",lst)
print("ID - списка:", id(lst))
print("-------------")

def multiply_list(lst, coeff):
    for i in range(len(lst)):
        #print(i, lst[i])
        lst[i] *= coeff

multiply_list(lst, 20)
print("Список коэффициента:", lst)
print("ID - списка:", id(lst))
print("-------------")

def nullify_list(lst):
    for i in range(len(lst)):
        lst[i] = 0

nullify_list(lst)
print("Нулевой список:", lst)
print("ID -  нулевого списка:", id(lst))
print("-------------")