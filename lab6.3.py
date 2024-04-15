students_languages = {
    'Иванов': ['английский', 'французский', 'немецкий'],
    'Петров': ['английский', 'китайский'],
    'Сидоров': ['испанский', 'итальянский'],
    'Козлов': ['китайский', 'японский'],
    'Смирнов': ['французский'],
    'Алексеев': ['английский', 'немецкий'],
}

all_languages = set()
for languages in students_languages.values():
    all_languages.update(languages)

num_languages = len(all_languages)
sorted_languages = sorted(all_languages)
print("Количество различных языков, которые знают студенты:", num_languages)
print("Отсортированный список языков, которые знают студенты:")
for language in sorted_languages:
    print(language)

chinese_speakers = [student for student, languages in students_languages.items() if 'китайский' in languages]
print("\nСтуденты, которые знают китайский язык:")
for student in chinese_speakers:
    print(student)