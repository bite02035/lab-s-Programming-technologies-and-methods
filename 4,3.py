from random import randint #Встроенная библиотечная функция сортировки.
import time

a = []
def sort(n):
    for i in range(n):
        a.append(randint(1, 99))
    tit1 = time.time()
    a.sort()
    tit2 = time.time()
    print('скорость обработки:', (tit2 - tit1))
    print(a)
sort(100)
sort(1000)
sort(2000)
sort(5000)
sort(10000)
