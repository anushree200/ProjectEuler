d=1  # 1 Jan 1900 = Monday → 1
ans=0

def leap(y):
    return y%4==0 and (y%100!=0 or y%400==0)

for y in range(1900,2001):
    for m in range(1,13):
        if y>=1901 and d%7==0:
            ans+=1
        
        if m in [1,3,5,7,8,10,12]:
            days=31
        elif m in [4,6,9,11]:
            days=30
        else:
            days=29 if leap(y) else 28
        
        d+=days

print(ans)