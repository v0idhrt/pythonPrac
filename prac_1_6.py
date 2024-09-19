def swap_columns(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]

n, m = map(int, input("Введите размеры массива n и m: ").split())

array = []

# Считываем элементы массива
for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)

i, j = map(int, input("Введите индексы столбцов i и j: ").split())

swap_columns(array, i, j)

for row in array:
    print(" ".join(map(str, row)))
