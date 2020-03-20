'''
Merge Sort는 분할 하는 루틴과 합치는 루틴으로 나뉘어진다.
'''


def MergeSort(s, e):
    if s == e:
        return
    if s < e:
        mid = (s+e)//2
        MergeSort(s, mid)
        MergeSort(mid+1, e)
        Merge(s, mid, e)


def Merge(s, mid, e):
    i, j, k = s, mid+1, s

    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            arr2[k] = arr[i]
            i += 1
            k += 1
        else:
            arr2[k] = arr[j]
            j += 1
            k += 1

    while i <= mid:
        arr2[k] = arr[i]
        i += 1
        k += 1

    while j <= e:
        arr2[k] = arr[j]
        j += 1
        k += 1

    for i in range(s, e+1):
        arr[i] = arr2[i]


arr = [1, 5, 3, 6, 8, 4, 3, 8, 2, 1, 5, 6]
arr2 = [0]*len(arr)
MergeSort(0, len(arr)-1)

print(arr)
print(arr2)
