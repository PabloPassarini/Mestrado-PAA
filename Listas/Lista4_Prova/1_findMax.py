def find_max(L):
    if len(L) == 1: return L[0]
    max_rec = find_max(L[1:])
    return L[0] if L[0] > max_rec else max_rec

print(find_max([1, 5, 3, 9, 2]))





print(len([0,1,2,3]))
print(len([[0,1,2,3], [0,1,2,3]]))