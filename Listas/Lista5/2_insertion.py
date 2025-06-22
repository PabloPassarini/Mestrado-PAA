def insertion(vec):

    for i in range(len(vec)):
        key = vec[i]
        j = i-1
        while (vec[j] > key) and (j >= 0):
            vec[j+1] = vec[j]
            j -= 1
        vec[j+1] = key 

    return vec

arr = [5, 3, 1, 8, 9, 4]
print(f'Array original: {arr}')
arr_s = insertion(arr)


print(f'Array ordenado: {arr_s}')

