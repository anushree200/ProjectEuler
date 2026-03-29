d={1:1}
ans=1
mx=1

for i in range(2,1000000):
    n=i
    c=0
    while n not in d:
        if n%2==0:
            n//=2
        else:
            n=3*n+1
        c+=1
    d[i]=c+d[n]
    if d[i]>mx:
        mx=d[i]
        ans=i

print(ans)