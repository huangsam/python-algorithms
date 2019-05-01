def lis(arr):
    longest = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                longest[i] = max(longest[i], longest[j] + 1)
    return max(longest)
