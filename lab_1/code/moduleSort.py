# Bubble sort
def bubble_sort(arr):
    comp = 0
    swaps = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            comp += 1
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, comp, swaps


def new_gap(gap, if_sorted):
    k = 1.247  # ~1/(1 - 1/(exp^fi))
    gap = int(gap // k)
    if gap <= 1:
        gap = 1
        if_sorted = True
    return gap, if_sorted


# Comb sort
def comb_sort(arr):
    comp = 0
    swaps = 0
    gap = len(arr)
    if_sorted = False
    while not if_sorted:
        gap, if_sorted = new_gap(gap, if_sorted)
        for i in range(len(arr) - gap):
            comp += 1
            if arr[i] > arr[i + gap]:
                swaps += 1
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                if_sorted = False
    return arr, comp, swaps
