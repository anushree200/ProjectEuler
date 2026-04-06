def sum_of_amicable(limit):
    d = [0] * (limit + 1)

    # Step 1: compute sum of proper divisors
    for i in range(1, limit):
        for j in range(2 * i, limit + 1, i):
            d[j] += i

    total = 0

    # Step 2: check amicable pairs
    for a in range(1, limit):
        b = d[a]
        if b != a and b <= limit and d[b] == a:
            total += a

    return total


print(sum_of_amicable(10000))