# Считываем количество школьников
num_students = int(input("Введите количество школьников: "))

#множество хранения языков, которые знают все школьники
common_languages = None

#знает хотя бы один школьник
all_languages = set()

for _ in range(num_students):
    # Считываем количество языков, которые знает школьник
    num_languages = int(input())
    
    languages = {input().strip() for _ in range(num_languages)}
    
    all_languages.update(languages)

    if common_languages is None: #если первый школьник
        common_languages = languages
    else:
        # Обновляем множество для общих языков (пересечение)
        common_languages.intersection_update(languages)

print(len(common_languages))
for lang in sorted(common_languages):
    print(lang)

print(len(all_languages))
for lang in sorted(all_languages):
    print(lang)
