def selection_sort(L):
    for i in range(len(L)):
        min_index = i
        for j in range(i+1, len(L)):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]

L = [5,3,8,1]
selection_sort(L)
print(L)
            
