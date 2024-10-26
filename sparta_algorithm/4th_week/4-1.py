
def mix(arr1, arr2):
    arr = arr1+arr2

    for i in range(len(arr)-1):
        scr = len(arr)-1-i
        for j in range(scr):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(mix(arr1, arr2))