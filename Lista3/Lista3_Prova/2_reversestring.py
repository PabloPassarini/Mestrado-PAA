def reverse_string(x):
    x = list(x)
    reverse = ''
    while x:
        reverse += x.pop()
    return reverse

 

print(reverse_string("Pablo"))