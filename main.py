import random

lst = random.sample(range(0, 50), 25)
endPoint = 1

print(lst)

while endPoint != len(lst) - 1:

    for i in range(endPoint, 0, -1):
        if lst[i] < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i-1], lst[i]
        elif lst[i] > lst[i - 1]:
            break
    
    endPoint += 1

print(lst)