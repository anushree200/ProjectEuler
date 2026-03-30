d={1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
d_teens={10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
d_tens={20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}

res=0
for i in range(1,1001):
    if i<10:
        res+=d[i]
    elif i<20:
        res+=d_teens[i]
    elif i<100:
        res+=d_tens[(i//10)*10]
        if i%10!=0:
            res+=d[i%10]
    elif i<1000:
        res+=d[i//100]+7
        if i%100!=0:
            res+=3
            j=i%100
            if j<10:
                res+=d[j]
            elif j<20:
                res+=d_teens[j]
            else:
                res+=d_tens[(j//10)*10]
                if j%10!=0:
                    res+=d[j%10]
    else:
        res+=3+8

print(res)