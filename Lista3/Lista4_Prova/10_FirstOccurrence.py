def first_occurrence(L, x, low=0, high=None):
    if high is None: high = len(L) - 1
    if low > high: return -1

    mid = (low + high) // 2
    if L[mid] == x:
        if mid == 0 or L[mid - 1] < x:
            return mid
        else:
            return first_occurrence(L, x, low, mid - 1)
    elif L[mid] < x:
        return first_occurrence(L, x, mid + 1, high)
    else:
        return first_occurrence(L, x, low, mid - 1)

print(first_occurrence([1, 2, 2, 2, 3, 4], 2))