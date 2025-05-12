def find_peak(L, low=0, high=None):
    if high is None: high = len(L) - 1
    
    mid = (low + high) // 2
    if (mid == 0 or L[mid] >= L[mid - 1]) and (mid == len(L) - 1 or L[mid] >= L[mid + 1]):
        return mid
    elif mid > 0 and L[mid - 1] > L[mid]:
        return find_peak(L, low, mid - 1)
    else:
        return find_peak(L, mid + 1, high)

print(find_peak([1, 3, 20, 4, 1, 0]))