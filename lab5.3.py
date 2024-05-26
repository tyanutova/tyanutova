days_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

num_weekend_days = int(input("Сколько выходных дней на неделе вы хотите? "))

weekend_days = days_of_week[-num_weekend_days:]
working_days = days_of_week[:-num_weekend_days]

print("Ваши выходные дни:", ', '.join(weekend_days))
print("Ваши рабочие дни:", ', '.join(working_days))