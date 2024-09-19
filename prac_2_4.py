
list1 = list(map(int, input("Введите первый список чисел через пробел: ").split()))
list2 = list(map(int, input("Введите второй список чисел через пробел: ").split()))

Находим общие числа и выводим их в порядке возрастания
common_numbers = sorted(set(list1) & set(list2))


print(" ".join(map(str, common_numbers)))
