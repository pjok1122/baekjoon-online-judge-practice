def binary_search(target):
    start = 0
    end = len(arr)-1
    while(start <= end):
        mid = (start+end)//2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return False


def binary_search_recursive(s, e, target):
    if s > e:
        return False

    mid = (s+e)//2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search_recursive(s, mid-1, target)
    else:
        return binary_search_recursive(mid+1, e, target)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(5))
