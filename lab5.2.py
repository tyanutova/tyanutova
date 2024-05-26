my_list = [3, 6, 8, 3, 2, 9, 6, 3]

def find_duplicates(lst):
    seen = set()
    duplicates = set(x for x in lst if x in seen or seen.add(x))
    return list(duplicates)

duplicates = find_duplicates(my_list)

if duplicates:
    print("Повторяющиеся элементы в списке:")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("В списке нет повторяющихся элементов.")