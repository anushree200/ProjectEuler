def recurring_cycle_length(n):
    remainder = 1
    remainders_seen = {}
    position = 0
    
    while remainder != 0 and remainder not in remainders_seen:
        remainders_seen[remainder] = position
        remainder = (remainder * 10) % n
        position += 1
    
    if remainder == 0:
        return 0
    else:
        return position - remainders_seen[remainder]


max_length = 0
max_n = 0

for i in range(1, 1000):
    cycle_length = recurring_cycle_length(i)
    if cycle_length > max_length:
        max_length = cycle_length
        max_n = i

print(f"{max_n}")