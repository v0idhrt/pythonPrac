n = int(input("Введите нечетное число n: "))

array = [["." for _ in range(n)] for _ in range(n)]

middle_index = n // 2

#Заполняем среднюю строку
for j in range(n):
    array[middle_index][j] = "*"

#Заполняем средний столбец
for i in range(n):
    array[i][middle_index] = "*"

#Заполняем главную диагональ
for i in range(n):
    array[i][i] = "*"

#Заполняем побочную диагональ
for i in range(n):
    array[i][n - 1 - i] = "*"

#Выводим полученный массив
for row in array:
    print(" ".join(row))
