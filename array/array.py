#  Q - 1 Find largest element in a array in one traversal

def largets_num(arr):
    current_ele = 0
    for i in range(0, len(arr)):
        if arr[i] > current_ele:
            current_ele = arr[i]
    return current_ele

print(largets_num([1, 8, 40, 3, 12]))