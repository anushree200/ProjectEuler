status=False
for a in range(1,1001):
    for b in range(a,1001):
        if(a*b -1000*a - 1000*b + 500000)!=0:
            continue
        c = 1000 - a - b
        if(a*a + b*b == c*c):
            ans = a*b*c
            status=True
            break
    if status:
        break
print(ans)