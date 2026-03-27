n_val = int(input("enter number: "))

d = 2
mx = -1

while d * d <= n_val:
    while n_val % d == 0:
        mx = d
        n_val //= d
    d += 1

if n_val > 1:
    mx = n_val

print(mx)