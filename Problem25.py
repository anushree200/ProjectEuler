# first fibonacci to cross 1000 digits
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 1
while len(str(fib(n))) < 1000:
    n += 1

print(n)