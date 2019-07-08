def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]

        # heapify root element
        heapify(arr, i, 0)
