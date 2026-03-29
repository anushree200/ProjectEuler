s=0
while True:
    try:
        x=input()
        s+=int(x[:15])
    except:
        break
print(str(s)[:10])