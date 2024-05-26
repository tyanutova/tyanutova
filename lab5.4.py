import random
import re
def ex54():
    myStudents = ["Воронков", "Петров", "Ключников", "Керган", "Молькова", "Михалев", "Торхов", "Тянутова", "Уланова", "Хачатрян"]
    '''otherStudents = ["Петров", "Иванов", "Добриков", "Процай", "Силантьева", "Лазарев", "Соменков", "Теплых", "Сорокина", "Макарин"]'''
    otherStudents = ["Петров", "Иванов", "Добриков", "Иванов", "Силантьева", "Иванов", "Соменков", "Иванов", "Сорокина", "Иванов"]

    team = []
    while len(team) != 10:
        i = random.randint(0, 9)
        indexI = []
        if (myStudents[i] not in team) or (myStudents[i] in team and i not in indexI):
            indexI.append(i)
            team.append(myStudents[i])
        j = random.randint(0, 9)
        indexJ = []
        if (otherStudents[j] not in team) or (otherStudents[j] in team and i not in indexJ):
            team.append(otherStudents[j])
    team = tuple(sorted(team))
    print(myStudents, "\n", otherStudents)
    print(team, "\n", len(team))
    if "Иванов" in team:
        print(len(re.findall("Иванов", str(team))))
ex54()