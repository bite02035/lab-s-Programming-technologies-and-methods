import numpy as np
import matplotlib.pyplot as plt
import time
import xlsxwriter


E=[]
for SortNumber in range(3):
    krug = 0
    print(SortNumber)
    while True:
        if krug == 0:
            n = 100
        elif krug == 1:
            n = 100
        elif krug == 2:
            n = 1000
        elif krug == 3:
            n = 2000
        elif krug == 4:
            n = 5000
        elif krug == 5:
            n = 10000
        else:
            break

        x = np.arange(1, n)
        y = np.random.randint(1, 100, size=n - 1)
        if krug == 0:
            plt.ion()
            fig, ax = plt.subplots()
            ax.bar(x, y)
            ax.set_facecolor('seashell')
            fig.set_facecolor('floralwhite')
            fig.set_figwidth(12)  # ширина Figure
            fig.set_figheight(6)  # высота Figure
        if krug != 0:
            plt.close()
        tit1 = time.time()

        if SortNumber == 0:
            for i in range(len(y) - 1):
                m = i
                j = i + 1
                while j < len(y):
                    if y[j] < y[m]:
                        m = j
                    j = j + 1
                y[i], y[m] = y[m], y[i]
                if krug == 0:
                    plt.clf()
                    plt.bar(x, y)
                    plt.draw()
                    plt.gcf().canvas.flush_events()
                    time.sleep(0.01)
            plt.close()
        elif SortNumber == 1:
            for i in range(len(y)):
                cursor = y[i]
                pos = i
                while pos > 0 and y[pos - 1] > cursor:
                    # Меняем местами число, продвигая по списку
                    y[pos] = y[pos - 1]
                    pos = pos - 1
                # Остановимся и сделаем последний обмен
                y[pos] = cursor
                if krug == 0:
                    plt.clf()
                    plt.bar(x, y)
                    plt.draw()
                    plt.gcf().canvas.flush_events()
                    time.sleep(0.01)
            plt.close()
        else:
            y.sort()

        tit2 = time.time()
        print(SortNumber, n)
        if krug != 0:
            ex = tit2 - tit1
            E.append(str(ex))
        krug += 1
plt.ioff()
plt.show()

# открываем новый файл на запись
workbook = xlsxwriter.Workbook('hello.xlsx')
# создаем там "лист"
worksheet = workbook.add_worksheet()
b=['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5']
for i in range (15):
    worksheet.write(b[i], E[i])
# сохраняем и закрываем
workbook.close()