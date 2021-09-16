row = []
n = int(input("Сколько строк необходимо вывести?\n"))
for i in range(n):
    row = [1] + row
    for i in range(1, len(row)-1):
        row[i] += row[i+1]
m=len(str(row))
row=[]
for i in range(n):
    row = [1] + row
    for i in range(1, len(row)-1):
        row[i] += row[i+1]
    print(str(row).center(m))
