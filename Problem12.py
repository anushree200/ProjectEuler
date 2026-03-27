def d(a):
    count=1
    i=2
    while i*i<=a:
        power=0
        while a%i==0:
            a//=i
            power+=1
        count*=(power+1)
        i+=1
    if a>1:
        count*=2
    return count

n=1
while True:
    if n%2==0:
        a=n//2
        b=n+1
    else:
        a=n
        b=(n+1)//2

    div = d(a)*d(b)

    if div>500:
        Tn = n*(n+1)//2
        print(Tn)
        break

    n+=1