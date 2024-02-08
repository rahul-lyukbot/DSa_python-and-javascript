# Question - find the index of x in a given array using binary search where x = 60 ?
arr = [10,20,30,40,50,60]


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half
    
    return -1  # Target not found
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 6

# result = binary_search(sorted_array, target_value)

# if result != -1:
#     print(f"Target {target_value} found at index {result}.")
# else:
#     print(f"Target {target_value} not found in the array.")


# Q - Find a given element using recurrsive binary search?

def recursive_binary_search(arr, target, low, high):
    if len(arr) == 1:
        return arr
    
    if low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return recursive_binary_search(arr, target, mid+1, high)
        else:
            return recursive_binary_search(arr, target, low, mid-1 )
    else:
        return -1


sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 6

# result = recursive_binary_search(sorted_array, target_value, 0 , len(arr)-1)

# if result != -1:
#     print(f"Target {target_value} found at index {result}.")
# else:
#     print(f"Target {target_value} not found in the array.")

# Question 2 - return index of first occurrence in sorted array?
def first_occurence(arr, target):
    if len(arr) == 1:
        return arr
    low , high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if(arr[mid] == target):
            if(arr[mid] == target or arr[mid-1] != target_value):
                return mid
            else:
                return mid-1
        elif arr[mid] < target:
                return recursive_binary_search(arr, target, mid+1, high)
        else:
                return recursive_binary_search(arr, target, low, mid-1 )
    return -1

arr = [10,20,20,30,30,40,50]
target_value = 30

# result = first_occurence(arr, target_value)

# if result != -1:
#     print(f"Target {target_value} found at index {result}.")
# else:
#     print(f"Target {target_value} not found in the array.")

    

# Question 3 - return index of last occurrence in sorted array?
def last_occurence(arr, target):
    if len(arr) == 1:
        return arr
    low , high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if(arr[mid] == target):
            if(arr[mid] == len(arr)-1 or arr[mid+1] != target_value):
                return mid
            else:
                return mid-1
        elif arr[mid] < target:
                return recursive_binary_search(arr, target, mid+1, high)
        else:
                return recursive_binary_search(arr, target, low, mid-1 )
    return -1

result = last_occurence(arr, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found in the array.")


# Question 4 - return the total occurrence of the given element in a given sorted array?
    
def total_occurence(arr, target):
    if len(arr) == 1:
        return arr
    low , high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2