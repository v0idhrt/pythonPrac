n, m = map(int, input().split())

array = []

for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)

max_value = float('-inf') 
max_index = (-1, -1)  

for i in range(n):
    for j in range(m):
        if array[i][j] > max_value:
            max_value = array[i][j]
            max_index = (i + 1, j + 1)  

print(max_index[0], max_index[1])
