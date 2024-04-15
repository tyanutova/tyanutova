countries_capitals = {
    'Россия': 'Москва',
    'США': 'Вашингтон',
    'Франция': 'Париж',
    'Германия': 'Берлин',
    'Великобритания': 'Лондон'
}

print("Содержимое словаря стран и их столиц:")
for country, capital in countries_capitals.items():
    print(country, "-", capital)

country_to_lookup = 'Россия'
if country_to_lookup in countries_capitals:
    print("Столица страны" ,{country_to_lookup}, ":", {countries_capitals[country_to_lookup]})
else:
    print("Страна" ,{country_to_lookup}, "не найдена в словаре.")

sorted_countries_capitals = {k: v for k, v in sorted(countries_capitals.items())}
print("Содержимое словаря после сортировки по названиям стран:")
for country, capital in sorted_countries_capitals.items():
    print(country, "-", capital)