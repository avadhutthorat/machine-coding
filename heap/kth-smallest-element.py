

import heapq

def kthSmallestElement(arr, k):
    # Solution 1
    # return heapq.nsmallest(k,arr)[-1]

    # Solution 2
    op = []
    for _, num in enumerate(arr):
        heapq.heappush(op, -num)
        if len(op) > k:
            heapq.heappop(op)
    return abs(op[0])



print(kthSmallestElement([7,10,4,3,20,15], 2))

