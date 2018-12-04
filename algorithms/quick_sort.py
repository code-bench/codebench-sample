def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quick_sort([x for x in arr[1:] if x < arr[0]]) \
               + [arr[0]] \
               + quick_sort([x for x in arr[1:] if x >= arr[0]])
