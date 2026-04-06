def sumofdigits(n):
    return sum(int(digit) for digit in str(n))

prod=1
for i in range(1,101):
    prod*=i

print(sumofdigits(prod))