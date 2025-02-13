def bubble_sort(L):
    for i in range(len(L)):
        for j in range(0, len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]


L = [5,3,8,1,0,10,4,6,9]
bubble_sort(L)
print(L)



