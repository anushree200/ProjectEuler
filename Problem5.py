import math

ans = 1
for i in range(1, 21):
    ans = ans * i // math.gcd(ans, i)

print(ans)