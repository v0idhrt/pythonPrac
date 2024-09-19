list1 = list(map(int, input("Введите первый список чисел через пробел: ").split()))
list2 = list(map(int, input("Введите второй список чисел через пробел: ").split()))

common_count = len(set(list1) & set(list2))

print(common_count)
