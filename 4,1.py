from random import randint #Сортировка простым выбором.
import time
a = []


def sort(n):
    for i in range(n):
        a.append(randint(1, 99))
    tit1 = time.time()
    for i in range(len(a) - 1):
        m = i
        j = i + 1
        while j < len(a):
            if a[j] < a[m]:
                m = j
            j = j + 1
        a[i], a[m] = a[m], a[i]
        tit2 = time.time()
    print('скорость обработки:', (tit2 - tit1))
sort(100)
sort(1000)
sort(2000)
sort(5000)
sort(10000)
