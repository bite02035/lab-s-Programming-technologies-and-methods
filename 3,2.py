import itertools
from random import randint
s = []
count = 0
while True:
    if count != 0:
        a = input("""Выберите действие:
1. Перебор элементов списка
2. Операция формирования списка
3. Вставка элемента в список
4. Удаление элемента
5. Перестановка элементов списка
6. Печать односвязного списка\n""")
    if a == "1":
       count = 1
       a = 1
    elif a == "2":
        n = int(input("Введите размер списка"))
        for i in range(n):
            s.append(randint(1, 10))
    elif a == "3":
        y = input("Элемент который надо вставить: ")
        s.append(y)
        print("Текущая список:", s)
    elif a == "4":
        d = input("Элемент который надо удалить: ")
        s.remove(d)
        print("Текущая список:", s)
    elif a == "5":
        n=7
        for i in itertools.permutations(s, n):
            print(i)
    elif a == "6":
        print("Текущая список:", s)
        a=0
    else:
        print("Действие указанно неправильно")
        a+=1