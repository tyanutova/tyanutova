score_table = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Щ': 10, 'Ъ': 10, 'Ф': 10
}

def calculate_word_score(word):
    total_score = 0
    for letter in word.upper():
        if letter in score_table:
            total_score += score_table[letter]

    return total_score

word = input("Введите слово для расчета его стоимости: ")
score = calculate_word_score(word)

print("Стоймость слова " ,{word},  "равна ", {score},  "очков.")
