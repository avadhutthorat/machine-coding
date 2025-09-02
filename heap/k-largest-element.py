import heapq

def kLargestElement(arr, k):
    op = []

    for idx,num in enumerate(arr):
        heapq.heappush(op, num)
        if len(op) > k:
            heapq.heappop(op)

    return op

print(kLargestElement([7,10,4,3,20,15], 3))        