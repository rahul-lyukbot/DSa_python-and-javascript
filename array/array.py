#  Q - 1 Find largest element in a array in one traversal
arr = [1, 8, 40, 3, 12]
arr2 = [1, 2, 3, 4, 8]


def largets_num(arr):
    current_ele = 0
    for i in range(0, len(arr)):
        if arr[i] > current_ele:
            current_ele = arr[i]
    return current_ele

# print(largets_num([1, 8, 40, 3, 12]))

# Q - 2 Check if the given array is sorted in increasing order or not

def is_sorted(arr):
    current_element  = arr[0]
    for i in arr:
        if current_element <= arr[i]:
            current_element = arr[i]
        return False
    return True

# print(is_sorted(arr2))

# Q - 3 Rverse a given array

def revers_array(arr):
    return arr[::-1]

# print(revers_array(arr))

# Q - 4 Move all zero to the end of the array

def move_all_zero_end(arr):
    count = 0
    for i in range(0, len(arr)):
        # check if current element is zero or not
        if arr[i] != 0:
            # if current element is zero then we move current element to the index where count is point 
            # and then change the count to the current iteration index
            arr[i], arr[count] = arr[count], arr[i]
            count +=1
    return arr



# print(move_all_zero_end([1,3,0,2,3,0,2,0]))

# Q - 5 Rotate a given array to the left by 1

def rotate_array(arr):
    if len(arr) <=1:
        return arr
    first_ele = arr[1-1]
    for i in range(len(arr)):
        arr[i-1] = arr[i] 
    arr[len(arr)-1] = first_ele

    return arr

print(rotate_array([1,2,3,4]))

# new_array = [1,2,3,4]
# print(new_array[0-1])