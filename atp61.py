# 6.1.py
# Хімчинський Орест
# Лабораторна робота No 6.1
# Пошук елементів одновимірного масиву ітераційним
# Варіант 15
import random

# створення масиву
def create(low, high, size):
    p = []
    for i in range(size):
        p.append(random.randint(low, high))
    return p

# вивід в термінал
def print_list(p):
    print('Список:', p)

# розрахунки
def calculation(p):
    index_list = []
    for i in range(len(p)):
        if p[i] < 0 and p[i] % 2 == 0:
            index_list.append(i)
        else:
            None
    return index_list

# кількість елементів, які підходять за критерієм
def amount(index_list):
    amnt = len(index_list)
    return amnt

# сума елементів, які підходять за критерієм
def summ(index_list, p):
    sum_number = 0
    for index in index_list:
        sum_number += p[index]
    return sum_number

# заміна елементів які підходять по критерію
def change(p, index_list):
    for index in index_list:
        p[index] = 0
    return p

# головна функція
def main():
    p = create(low=int('-20'), high=int('34'), size=int('20'))
    print_list(p)
    index_list = calculation(p)
    amnt = amount(index_list)
    sum = summ(index_list, p)
    p = change(p, index_list)
    print(f'Кількість елементів, які підходять за критерієм: {amnt}\n'
          f'Сума елементів, які підходять за критерієм: {sum}')
    print_list(p)


main()

