queue = []
queue.append("1")
queue.append("2")
queue.append("3")
queue.append("4")
queue.append("5")
queue.append("6")

while True:
    a = 0
    print("Текущая очередь:\n", queue)
    a = input("""Выберите действие:
1. Поместить элемент х в конец очереди
2. Удаляет элемент из начала очереди queue и присваивает его значение переменной x
3. Вернуть значение FALSE если очередь является пустой, в ином случае вывесть TRUE
4. Определение текущего числа элементов в очереди
5. Очистка очереди\n""")
    if a == "1":
        x = input("Введите x ")
        queue.insert(len(queue), x)#                    так не правильно
        #queue.append(x) ###########################    правильно так
    elif a == "2":
        pass

    elif a == "3":
        pass

    elif a == "4":
        pass

    elif a == "5":
        pass

    else:
        print("Действие указанно неправильно")