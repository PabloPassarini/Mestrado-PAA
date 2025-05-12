def fib_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    l = [0, 1]
    for i in range(2, n + 1):  # vai até n, inclusive
        l.append(l[i-1] + l[i-2])
    return l[n]


print(fib_memo(10))