def calcscore(name):
    score = 0
    for c in name:
        score += ord(c) - ord('A') + 1
    return score

with open('0022_names.txt', 'r') as f:
    listnames = f.read().replace('"', '').split(',')

listnames.sort()

ans = 0
for i, name in enumerate(listnames, start=1):
    ans += calcscore(name) * i

print(ans)