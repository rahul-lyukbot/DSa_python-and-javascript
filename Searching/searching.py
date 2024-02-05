# Question - find the index of x in a given array using binary search where x = 60 ?
arr = [10,20,30,40,50,60]


def binary_serach(arr, x):
    if len(arr)<=1:
        return arr
    arr.sort()
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low+high)//2
        print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid-1] > x:
            low = mid+1
        else:
            high = mid-1

    return -1
    
print(binary_serach(arr, 50))


# Q - Find a given element using recurrsive binary search?

