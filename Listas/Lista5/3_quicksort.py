def partition(v, left, right):
    pivo = v[right]
    i = left - 1
    for j in range(left, right):
        if pivo > v[j]:
            i += 1
            v[i], v[j] = v[j], v[i]
    v[i+1], v[right] = v[right], v[i+1]
    print(v)
    return i+1


def quick(v, left, right):
    if left < right:
        q = partition(v, left, right)
        quick(v, left, q - 1)
        quick(v, q+1, right)

arr = [5, 3, 1, 8, 9, 4]
quick(arr, 0, len(arr) - 1)