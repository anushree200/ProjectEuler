n = 28123

div_sum = [0] * (n + 1)

for i in range(1, n//2 + 1):
    for j in range(2*i, n + 1, i):
        div_sum[j] += i

abundant = [i for i in range(1, n + 1) if div_sum[i] > i]

can = [False] * (n + 1)

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        s = abundant[i] + abundant[j]
        if s <= n:
            can[s] = True
        else:
            break

ans = sum(i for i in range(1, n + 1) if not can[i])

print(ans)