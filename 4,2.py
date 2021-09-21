from random import randint #Сортировка вставками
import time
a = []
def sort(n):
    for i in range(n):
        a.append(randint(1, 99))
    tit1 = time.time()
    for i in range(len(a)):
        cursor = a[i]
        pos = i
        while pos > 0 and a[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            a[pos] = a[pos - 1]
            pos = pos - 1
        # Остановимся и сделаем последний обмен
        a[pos] = cursor
    tit2 = time.time()
    print('скорость обработки:', (tit2 - tit1))
sort(100)
sort(1000)
sort(2000)
sort(5000)
sort(10000)