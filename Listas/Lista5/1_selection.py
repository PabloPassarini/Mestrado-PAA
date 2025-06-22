def selection(arr):
    for i in range(len(arr)-1):
        min_pos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_pos]: 
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

print(selection([3,4,5,1,6,2]))

