
N, M = map(int, input("Введите количество кубиков у Ани и Бори: ").split())


anya_colors = {int(input()) for _ in range(N)}
borya_colors = {int(input()) for _ in range(M)}

common_colors = anya_colors & borya_colors

only_anya_colors = anya_colors - borya_colors
only_borya_colors = borya_colors - anya_colors


print(len(common_colors), *sorted(common_colors))
print(len(only_anya_colors), *sorted(only_anya_colors))
print(len(only_borya_colors), *sorted(only_borya_colors))
