N, K = map(int, input().split())

strike_days = set()

for _ in range(K):
    a_i, b_i = map(int, input().split())
    
    for day in range(a_i, N + 1, b_i):
        if day % 7 != 6 and day % 7 != 0: 
            strike_days.add(day)

print(len(strike_days))
for day in sorted(strike_days):
    print(day)
