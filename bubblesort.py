def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def printArray(arr):
    for x in arr:
        print(x, end=" ")
    print()

arr = [5, 1, 4, 2, 8]
bubbleSort(arr)
print("Sorted array:")
printArray(arr)
