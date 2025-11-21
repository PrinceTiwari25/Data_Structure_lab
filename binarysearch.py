def binarySearch(arr, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binarySearch(arr, x, low, mid - 1)
        return binarySearch(arr, x, mid + 1, high)

    return -1

arr = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch(arr, x, 0, len(arr) - 1)

if result == -1:
    print("Not found")
else:
    print("Element is found at index", result)
