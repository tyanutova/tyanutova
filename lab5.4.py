group1 = ['Иванов', 'Петров', 'Сидоров', 'Козлов', 'Смирнов', 'Алексеев', 'Николаев', 'Кузнецов', 'Морозов', 'Васильев']
group2 = ['Федоров', 'Григорьев', 'Дмитриев', 'Калинин', 'Павлов', 'Лебедев', 'Захаров', 'Белов', 'Гаврилов', 'Титов']

sports_team = tuple(group1[:5] + group2[:5])

print("Список студентов группы 1:", group1)
print("Список студентов группы 2:", group2)
print("Спортивная команда:", sports_team)

print("Длина спортивной команды:", len(sports_team))

sorted_team = sorted(sports_team)
print("Отсортированная спортивная команда:", sorted_team)

surname_to_check = "Иванов"
count_ivanov = sports_team.count(surname_to_check)
if count_ivanov > 0:
    print("Студент с фамилией", {surname_to_check}," находится в спортивной команде.")
    print("Количество вхождений фамилии", {surname_to_check}, " в команду: {count_ivanov}")
else:
    print("Студент с фамилией" ,{surname_to_check}, "не находится в спортивной команде.")