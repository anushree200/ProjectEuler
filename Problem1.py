s=0
for i in range(1,1001):
    if(i%3==0):
        s+=i
        continue
    elif (i%5==0):
        s+=i
print(s)