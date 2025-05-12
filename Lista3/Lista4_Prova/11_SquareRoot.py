def sqrt_binary(n, low=0, high=None):
    if high is None:
        high = n
    if low > high:
        return high
    mid = (low + high) // 2
    if mid * mid == n:
        return mid
    elif mid * mid < n:
        return sqrt_binary(n, mid + 1, high)
    else:
        return sqrt_binary(n, low, mid - 1)


print(sqrt_binary(10))

print(sqrt_binary(16))