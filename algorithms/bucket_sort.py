def bucket_sort(arr):
    buckets = [0] * ((max(arr) - min(arr))+1)
    for i in range(len(arr)):
        buckets[arr[i]-min(arr)] += 1
    res=[]
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+min(arr)]*buckets[i]
    return res

