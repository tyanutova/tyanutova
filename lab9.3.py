def z3():
    file = open('данные.csv', 'r', encoding='utf-8')
    data = list(csv.reader(file, delimiter=","))
    print("Список товаров: ")
    for i in data:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб")
    print(f"Итоговая цена: {sum([int(i[1]) * int(i[2]) for i in data])} руб.")
z3()