def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right, buffer):
    if arr[mid] <= arr[mid + 1]:
        return

    i, j = left, mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            buffer[k] = arr[i]
            i += 1
        else:
            buffer[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        buffer[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        buffer[k] = arr[j]
        j += 1
        k += 1

    arr[left:right + 1] = buffer[left:right + 1]


def timsort(arr):
    n = len(arr)
    min_run = 32

    buffer = [0] * n

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(left + size - 1, n - 1)
            right = min(left + size * 2 - 1, n - 1)

            if mid < right:
                merge(arr, left, mid, right, buffer)

        size *= 2
