import itertools
from random import randint
count = 1
a=0
while True:
    if count != 0:
        a = input("""Выберите действие:
1. Перебор элементов списка
2. Операция формирования списка
3. Вставка элемента в список
4. Удаление элемента
5. Перестановка элементов списка
6. Печать односвязного списка\n""")
    if str(a) == "1":
       count = 0
    elif str(a) == "2":
        s = []
        n = int(input("Введите размер списка"))
        for i in range(n):
            s.append(randint(1, 100))
    elif str(a) == "3":
        y = input("Элемент который надо вставить: ")
        s.append(int(y))
    elif str(a) == "4":
        d = int(input("Элемент который надо удалить: "))
        s.pop(d)
    elif str(a) == "5":
        first = int(input("Укажите порядковый номер первого элемента"))
        second = int(input("Укажите порядковый номер первого элемента"))
        s[first], s[second] = s[second], s[first]
    elif str(a) == "6":
        a=0
        count = 1
    else:
        print("Действие указанно неправильно")
        print(a)
    a = int(a) + 1
    print("Текущий список:", s)
