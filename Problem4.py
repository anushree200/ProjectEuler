m = 0

for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        p = a * b
        
        if p <= m:
            break
        
        if str(p) == str(p)[::-1]:
            m = p

print(m)