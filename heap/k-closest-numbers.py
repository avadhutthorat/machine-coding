import heapq

def kClosestNumbers(arr, k, x):
    op = []
    targetIndex = arr.index(x)
    for idx, num in enumerate(arr):
        print(idx, targetIndex, num)
        heapq.heappush(op, (-abs(x - num), num))
        if len(op) > k:
            heapq.heappop(op)    

    op = [t[1] for t in op]
    return op


print(kClosestNumbers([5,6,7,8,9], 4,6))    