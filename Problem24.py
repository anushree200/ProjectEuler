import math

d = list(range(10))
k = 999999
ans = ""

for i in range(9, -1, -1):
    f = math.factorial(i)
    idx = k // f
    ans += str(d[idx])
    d.pop(idx)
    k %= f

print(ans)