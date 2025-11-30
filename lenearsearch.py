def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = []
print("Enter 10 Numbers:")
for _ in range(10):
    arr.append(int(input()))

x = int(input("Enter a Number to Search: "))
index = linear_search(arr, x)

if index != -1:
    print("Found at Index No.", index)
else:
    print("Number not found")
