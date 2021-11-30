month = {'01': 0, '02': 31, '03': 59, '04': 90, '05': 120, '06': 151, '07': 181, '08': 212, '09': 243, '10': 273,
         '11': 304, '12': 334}
year = 365
print("Определение расстояния в днях между двумя произвольными датами\nФормат ввода дд.мм.гггг")#проверка на сайте https://seolik.ru/date-difference
while True:
    a = "01.11.1917" #input("Введите первую дату ")
    b = "01.12.2021" #input("Введите вторую дату ")
    print(a)
    if len(a) < 7 or len(b) < 7 or a[2] != "." or a[5] != "." or b[2] != "." or b[5] != ".":
        print('Проверь поле ввода!')
    else:
        break
if int(a[6:]) < int(b[6:]):
    a, b = b, a
d1 = int(a[0:2])
m1 = a[3:5]
y1 = int(a[6:])
d2 = int(b[0:2])
m2 = b[3:5]
y2 = int(b[6:])
m_days_a = month.get(m1)
m_days_b = month.get(m2)
days_a = d1 + int(m_days_a) + (y1 * year)
days_b = d2 + int(m_days_b) + (y2 * year)
days = days_a - days_b
if days < 0:
    days = -days
if y1 < y2:
    y1, y2 = y2, y1
for i in range(int(y2+1), int(y1), 1):# проверка на високосность
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        days +=1
print(days)
