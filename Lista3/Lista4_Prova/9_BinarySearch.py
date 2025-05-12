def binary_search(L, x, low=0, high=None):
    if high is None:
        high = len(L) - 1
    if low > high:
        return False
    mid = (low + high) // 2
    if L[mid] == x:
        return True
    elif L[mid] < x:
        return binary_search(L, x, mid + 1, high)
    else:
        return binary_search(L, x, low, mid - 1)

print(binary_search([1, 3, 5, 7, 9], 3))
print(binary_search([1, 3, 5, 7, 9], 4))